from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic import View

from apps.products.models import Product


class HealthView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"status": "ok"}, status=200)


class HomeView(TemplateView):
    template_name = "products/index.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context["products"] = Product.objects.all().order_by("-created_at")[:6]
        context["active"] = "home"
        return render(request, self.template_name, context=context)


class ProductsView(ListView):
    paginate_by = 6
    model = Product
    queryset = Product.objects.all()
    template_name = "products/products.html"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response.context_data["active"] = "products"
        return response


class ProductDetailView(DetailView):
    model = Product
    queryset = Product.objects.all()
    template_name = "products/product.html"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response.context_data["active"] = "products"
        response.context_data["images"] = response.context_data[
            "object"
        ].productimage_set.filter(enable=True)
        return response


class AboutUsView(TemplateView):
    template_name = "products/about.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context["active"] = "about"
        return render(request, self.template_name, context=context)


class ContactsView(TemplateView):
    template_name = "products/contact.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context["active"] = "contacts"
        return render(request, self.template_name, context=context)
