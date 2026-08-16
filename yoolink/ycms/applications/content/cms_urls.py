from django.urls import path

from . import views
from yoolink.ycms.permissions import cms_permission_required

pages_required = cms_permission_required("pages.edit")

urlpatterns = [
    path("", pages_required(views.content_view), name="sites"),
    path("save/", pages_required(views.save_text_content), name="save_text_content"),
    path("hauptseite/", pages_required(views.site_view_main), name="site_hauptseite"),
    path("datenschutz/", pages_required(views.site_view_datenschutz), name="site_datenschutz"),
    path("datenschutz/save/", pages_required(views.save_privacy_policy), name="save_privacy_policy"),
    path("impressum/", pages_required(views.site_view_impressum), name="site_impressum"),
    path("impressum/save/", pages_required(views.save_impressum), name="save_impressum"),
    path("cookies/", pages_required(views.site_view_cookies), name="site_cookies"),
    path("blog/", pages_required(views.site_view_blog_overview), name="site_blog_overview"),
]
