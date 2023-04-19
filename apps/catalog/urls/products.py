from django.urls import re_path

from apps.catalog.views import (
    ProductListView,
    ProductDetailSlugView,
    ProductDownloadView,
)

urlpatterns = [
    re_path(r"^$", ProductListView.as_view(), name="list"),
    re_path(r"^(?P<slug>[\w-]+)/$", ProductDetailSlugView.as_view(), name="detail"),
    re_path(
        r"^(?P<slug>[\w-]+)/(?P<pk>\d+)/$",
        ProductDownloadView.as_view(),
        name="download",
    ),
]
