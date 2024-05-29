from django.shortcuts import render
from django.apps import apps
'''
def cart(request):
    Order = apps.get_model('customer', 'Order')  # Припустимо, що ваша модель є в додатку customer

    # Отримуємо всі замовлення для поточного користувача (якщо він аутентифікований)
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user)
    else:
        orders = None

    # Передаємо список замовлень на сторінку cart.html для відображення
    return render(request, 'cart.html', {'orders': orders})
'''