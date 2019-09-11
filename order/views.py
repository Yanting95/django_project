from django.shortcuts import render, get_object_or_404
from .models import Order, OrderItem
from kitchen.models import Kitchen, Dish
from django.contrib.auth.models import User
from .forms import OrderCreateForm
# from .tasks import order_created
from cart.cart import Cart
from .email import order_created
from django.contrib.auth.decorators import login_required


@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            kitchen = cart.get_provider()
            order.provider = kitchen
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         dish=item['dish'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task
            # order_created.delay(order.id)
            order_created(order.id)
            return render(request, 'order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'order/create.html', {'cart': cart,
                                                 'form': form})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order,pk=order_id)
    items = OrderItem.objects.filter(order=order_id)
    # kitchen = Kitchen.objects.get(pk=order.provider)
    # dishes = Dish.objects.filter(pk__in=items.dish)
    return render(request, 'order/order_detail.html', {'order': order, 'items': items})


@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order/order_list.html', {'orders': orders})

