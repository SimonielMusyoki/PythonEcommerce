from django.conf import settings
from django.conf.urls.static import static

from django.urls import re_path, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView, RedirectView


from apps.accounts.views import (
    LoginView,
    RegisterView,
    GuestRegisterView,
    AddressCreateView,
    AddressListView,
    AddressUpdateView,
    checkout_address_create_view,
    checkout_address_reuse_view,
)
from apps.analytics.views import SalesView, SalesAjaxView
from apps.orders.views import payment_method_view, payment_method_createview
from apps.orders.views import cart_detail_api_view
from apps.marketing.views import MarketingPreferenceUpdateView, MailchimpWebhookView
from apps.orders.views import LibraryView

from .views import home_page, about_page, contact_page

urlpatterns = [
    re_path(r"^$", home_page, name="home"),
    re_path(r"^about/$", about_page, name="about"),
    # re_path(r'^accounts/login/$', RedirectView.as_view(url='/login')),
    re_path(r"^accounts/$", RedirectView.as_view(url="/account")),
    re_path(r"^account/", include("apps.accounts.urls", namespace="account")),
    re_path(r"^accounts/", include("apps.accounts.passwords.urls")),
    re_path(r"^address/$", RedirectView.as_view(url="/addresses")),
    re_path(r"^addresses/$", AddressListView.as_view(), name="addresses"),
    re_path(r"^addresses/create/$", AddressCreateView.as_view(), name="address-create"),
    re_path(
        r"^addresses/(?P<pk>\d+)/$", AddressUpdateView.as_view(), name="address-update"
    ),
    re_path(r"^analytics/sales/$", SalesView.as_view(), name="sales-analytics"),
    re_path(
        r"^analytics/sales/data/$", SalesAjaxView.as_view(), name="sales-analytics-data"
    ),
    re_path(r"^contact/$", contact_page, name="contact"),
    re_path(r"^login/$", LoginView.as_view(), name="login"),
    re_path(
        r"^checkout/address/create/$",
        checkout_address_create_view,
        name="checkout_address_create",
    ),
    re_path(
        r"^checkout/address/reuse/$",
        checkout_address_reuse_view,
        name="checkout_address_reuse",
    ),
    re_path(r"^register/guest/$", GuestRegisterView.as_view(), name="guest_register"),
    re_path(r"^logout/$", LogoutView.as_view(), name="logout"),
    re_path(r"^api/cart/$", cart_detail_api_view, name="api-cart"),
    re_path(r"^cart/", include("apps.orders.urls.cart", namespace="cart")),
    re_path(
        r"^billing/payment-method/$", payment_method_view, name="billing-payment-method"
    ),
    re_path(
        r"^billing/payment-method/create/$",
        payment_method_createview,
        name="billing-payment-method-endpoint",
    ),
    re_path(r"^register/$", RegisterView.as_view(), name="register"),
    re_path(
        r"^bootstrap/$", TemplateView.as_view(template_name="bootstrap/example.html")
    ),
    re_path(r"^library/$", LibraryView.as_view(), name="library"),
    re_path(r"^orders/", include("apps.orders.urls.orders", namespace="orders")),
    re_path(r"^products/", include("apps.catalog.urls.products", namespace="products")),
    re_path(r"^search/", include("apps.catalog.urls.search", namespace="search")),
    re_path(r"^settings/$", RedirectView.as_view(url="/account")),
    re_path(
        r"^settings/email/$",
        MarketingPreferenceUpdateView.as_view(),
        name="marketing-pref",
    ),
    re_path(
        r"^webhooks/mailchimp/$",
        MailchimpWebhookView.as_view(),
        name="webhooks-mailchimp",
    ),
    re_path(r"^admin/", admin.site.urls),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
