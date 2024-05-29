from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from customer.models import Product

class AdminProductListView(ListView):
    model = Product
    template_name = 'admin_product_list.html'
    context_object_name = 'products'

class AdminProductCreateView(CreateView):
    model = Product
    template_name = 'admin_product_form.html'
    fields = ['name', 'description', 'price', 'image', 'quantity']
    success_url = reverse_lazy('admin_products')

class AdminProductUpdateView(UpdateView):
    model = Product
    template_name = 'admin_product_form.html'
    fields = ['name', 'description', 'price', 'image', 'quantity']
    success_url = reverse_lazy('admin_products')
