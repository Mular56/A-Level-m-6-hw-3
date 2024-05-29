from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView, FormView, ListView
from django.urls import reverse_lazy
from .models import Product, Customer
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'base.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') 
    template_name = 'signup.html' 
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.wallet = 10000
        self.object.save()
        return response
    

class MyLoginView(FormView):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        if user.is_superuser:
            return redirect('admin_products')
        return redirect(self.get_success_url())
    
'''class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    login_url = reverse_lazy('login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context'''
    
    
class ProductListView(ListView):
    model = Product
    template_name_authenticated = 'product_list.html'
    template_name_unauthenticated = 'product_list_unauth.html'
    context_object_name = 'products'
    login_url = reverse_lazy('login')

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return [self.template_name_authenticated]
        else:
            return [self.template_name_unauthenticated]
        
        
'''def personal_cabinet(request):
    if request.user.is_authenticated:
        customer = Customer.objects.get(user=request.user)
        return render(request, 'personal_cabinet.html', {'customer': customer})
    else:
        return render(request, 'not_authenticated.html')'''
    
@login_required
def personal_cabinet(request):
    try:
        customer = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        # Якщо екземпляр Customer не знайдено, можна зробити щось інше, наприклад, перенаправити користувача на сторінку створення профілю
        return redirect('create_profile')  # Припустимо, що 'create_profile' - це URL для створення профілю

    # Тут ви можете використовувати 'customer' для передачі даних у шаблон

    return render(request, 'personal_cabinet.html', {'customer': customer})
    