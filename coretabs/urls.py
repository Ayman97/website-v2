"""coretabs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView
from allauth.account.views import confirm_email

from hacks.views import password_reset_from_key, logout_view,\
    user_details_view, resend_confirmation_view, verify_email
from contact.views import contact_view

from discourse import views

import debug_toolbar

from rest_framework_cache.registry import cache_registry


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/contact/', contact_view),

    path('api/v1/auth/logout/', logout_view),
    path('api/v1/auth/user/', user_details_view),
    path('api/v1/auth/confirmation/', resend_confirmation_view),
    path('api/v1/auth/registration/verify-email/', verify_email),
    path('api/v1/auth/', include('rest_auth.urls')),
    path('api/v1/auth/registration/', include('rest_auth.registration.urls')),
    path('discourse/sso', views.sso),

    path('api/v1/', include('library.urls')),

    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('__debug__/', include(debug_toolbar.urls)),

    url(r"^reset-password/(?P<uidb36>[0-9A-Za-z]+)/(?P<key>.+)/$",
        password_reset_from_key,
        name="account_reset_password_from_key"),
    url(r"^confirm-account/(?P<key>[-:\w]+)/$", confirm_email,
        name="account_confirm_email"),
]

cache_registry.autodiscover()
