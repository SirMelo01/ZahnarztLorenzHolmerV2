from django.conf import settings
from django.conf.urls.i18n import i18n_patterns, set_language
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token

from yoolink.sitemaps import BlogSitemap, StaticViewSitemap
from yoolink.views import (
    cookies_view,
    datenschutz_view,
    impressum_view,
    load_index,
)

sitemaps = {
    "static": StaticViewSitemap,
    "blog": BlogSitemap,
}

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/", include("config.api_router")),
    path("auth-token/", obtain_auth_token),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="api-schema"), name="api-docs"),
    path("i18n/setlang/", set_language, name="set_language"),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
        name="robots",
    ),
    path("cms/", include("yoolink.ycms.urls", namespace="ycms")),
    path("", include("django.contrib.auth.urls")),
]

urlpatterns += i18n_patterns(
    path("", view=load_index, name="home"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path("impressum/", view=impressum_view, name="impressum"),
    path("datenschutz/", view=datenschutz_view, name="datenschutz"),
    path("cookies/", view=cookies_view, name="cookies"),
    path("blog/", include("yoolink.blog.urls", namespace="blog")),
    path("users/", include("yoolink.users.urls", namespace="users")),
    prefix_default_language=False,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
