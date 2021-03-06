from django.contrib.admin import AdminSite
from django.contrib.admin.helpers import ActionForm
from django.forms import CharField
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import reverse
from django.views.decorators.cache import never_cache

from functools import update_wrapper
from django.views.decorators.csrf import csrf_protect

from coretabs import settings


class MyActionForm(ActionForm):
    x = CharField(required=False)


class MyAdminSite(AdminSite):

    @never_cache
    def login(self, request, extra_context=None):
        if request.method == 'GET' and self.has_permission(request):
            # Already logged-in, redirect to admin index
            index_path = reverse('admin:index', current_app=self.name)
            return HttpResponseRedirect(index_path)

        raise Http404

    def admin_view(self, view, cacheable=False):
        def inner(request, *args, **kwargs):
            if not self.has_permission(request):
                raise Http404
            return view(request, *args, **kwargs)

        if not cacheable:
            inner = never_cache(inner)
        # We add csrf_protect here so this function can be used as a utility
        # function for any view, without having to repeat 'csrf_protect'.
        if not getattr(view, 'csrf_exempt', False):
            inner = csrf_protect(inner)
        return update_wrapper(inner, view)


if settings.IS_PRODUCTION:
    site = MyAdminSite()
else:
    site = AdminSite()
