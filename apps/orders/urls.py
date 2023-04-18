from django.conf.urls import url

from .views.orders import OrderListView, OrderDetailView, VerifyOwnership
from .views.carts import cart_home, cart_update, checkout_home, checkout_done_view

urlpatterns = [
    url(r"^$", OrderListView.as_view(), name="list"),
    url(
        r"^endpoint/verify/ownership/$",
        VerifyOwnership.as_view(),
        name="verify-ownership",
    ),
    url(r"^(?P<order_id>[0-9A-Za-z]+)/$", OrderDetailView.as_view(), name="detail"),
    url(r"^$", cart_home, name="home"),
    url(r"^checkout/success/$", checkout_done_view, name="success"),
    url(r"^checkout/$", checkout_home, name="checkout"),
    url(r"^update/$", cart_update, name="update"),
]
