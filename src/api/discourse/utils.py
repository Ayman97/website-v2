import base64
import hmac
import hashlib
from urllib import parse

import requests

from django.conf import settings
from django.utils.module_loading import import_string


def get_avatar_url(user, size=settings.AVATAR_DEFAULT_SIZE):
    for provider_path in settings.AVATAR_PROVIDERS:
        provider = import_string(provider_path)
        avatar_url = provider.get_avatar_url(user, size)
        if avatar_url:
            if provider_path == 'avatar.providers.PrimaryAvatarProvider':
                avatar_url = settings.API_BASE_URL + avatar_url
            return avatar_url


def sync_sso(user):
    params = {
        'email': user.email,
        'external_id': user.id,
        'username': user.username,
        'name': user.first_name,
        'avatar_url': get_avatar_url(user),
        'avatar_force_update': True
    }

    key = bytes(settings.DISCOURSE_SSO_SECRET, encoding='utf-8')
    return_payload = base64.b64encode(bytes(parse.urlencode(params), 'utf-8'))
    h = hmac.new(key, return_payload, digestmod=hashlib.sha256)
    query_string = parse.urlencode(
        {'sso': return_payload, 'sig': h.hexdigest()})

    data = {'api_key': settings.DISCOURSE_API_KEY,
            'api_username': settings.DISCOURSE_API_USERNAME}

    url = f'{settings.DISCOURSE_BASE_URL}/admin/users/sync_sso/?{query_string}'

    r = requests.post(url, data=data)


def discourse_logout(user_id):
    data = {'api_key': settings.DISCOURSE_API_KEY,
            'api_username': settings.DISCOURSE_API_USERNAME}

    user = requests.get(settings.DISCOURSE_BASE_URL +
                        f'/users/by-external/{user_id}.json', data=data)

    user = user.json()
    user_id = user['user']['id']

    url = settings.DISCOURSE_BASE_URL + f'/admin/users/{user_id}/log_out/'

    r = requests.post(url, data=data)
