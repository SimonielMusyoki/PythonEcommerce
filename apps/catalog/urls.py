from django.conf.urls import url

from .views import (
    ProductListView,
    ProductDetailSlugView,
    ProductDownloadView,
    SearchProductView,
)

urlpatterns = [
    url(r"^$", ProductListView.as_view(), name="list"),
    url(r"^(?P<slug>[\w-]+)/$", ProductDetailSlugView.as_view(), name="detail"),
    url(
        r"^(?P<slug>[\w-]+)/(?P<pk>\d+)/$",
        ProductDownloadView.as_view(),
        name="download",
    ),
    url(r"^$", SearchProductView.as_view(), name="query"),
]
