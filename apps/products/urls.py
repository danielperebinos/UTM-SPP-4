from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from apps.products.views import HomeView, ProductsView, AboutUsView, ContactsView, ProductDetailView

urlpatterns = [
    path(r'', HomeView.as_view(), name="home"),
    path(r'products', ProductsView.as_view(), name="products"),
    path(r'product/<int:pk>', ProductDetailView.as_view(), name="product"),
    path(r'about-us', AboutUsView.as_view(), name="about"),
    path(r'contacts', ContactsView.as_view(), name="contacts"),
]