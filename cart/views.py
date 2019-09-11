from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from kitchen.models import Dish
from .cart import Cart
from .forms import CartAddForm
from django.contrib import messages


@require_POST
def cart_add(request, dish_id):
    cart = Cart(request)
    dish = get_object_or_404(Dish, id=dish_id)
    # for item in cart:
    #     kitchen = item['dish'].kitchen
    if cart.__len__() != 0 and dish.kitchen != cart.get_provider():
        messages.error(request, 'Cannot add dishes from different kitchen.')
    else:
        form = CartAddForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(dish=dish,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, dish_id):
    cart = Cart(request)
    dish = get_object_or_404(Dish, id=dish_id)
    cart.remove(dish)
    messages.success(request, 'Remove dishes successfully.')
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddForm(initial={'quantity': item['quantity'],
                                                            'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:cart_detail')