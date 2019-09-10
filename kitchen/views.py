from django.shortcuts import render, redirect, get_object_or_404
from . models import Kitchen, Dish
from . forms import KitchenForm, DishForm
from cart.forms import CartAddForm

def kitchen_list(request):
    kitchens = Kitchen.objects.all()
    return render(request,'kitchen/kitchen_list.html',{'kitchen_list':kitchens})


def kitchen_details(request,pk):
    kitchen = get_object_or_404(Kitchen,pk=pk)
    return render(request,'kitchen/kitchen_detail.html',{'kitchen':kitchen})


def kitchen_new(request):
    if request.method == "POST":
        form = KitchenForm(request.POST)
        if form.is_valid():
            kitchen = form.save(commit=False)
            kitchen.save()
            return redirect('kitchen:kitchen_details',pk=kitchen.pk)
    else:
        form = KitchenForm()
    return render(request,'kitchen/form.html',{'form':form})


def dish_list(request,pk):
    dishes = Dish.objects.filter(kitchen = pk)
    return render(request,'kitchen/dish_list.html',{'dish_list':dishes})


def dish_details(request,pkk,pk):
    dish = get_object_or_404(Dish,pk=pk)
    kitchen = get_object_or_404(Kitchen,pk=pkk)
    cart_add_form = CartAddForm()
    return render(request,'kitchen/dish_detail.html',{'dish':dish,
                                                      'kitchen':kitchen,
                                                      'cart_add_form': cart_add_form})


def dish_new(request,pk):
    if request.method == "POST":
        form = DishForm(request.POST)
        if form.is_valid():
            dish = form.save(commit=False)
            dish.kitchen = Kitchen.objects.get(id=pk)
            dish.save()
            return redirect('kitchen:dish_details',pkk=dish.kitchen.pk,pk=dish.pk)
    else:
        form = DishForm()
    return render(request,'kitchen/form.html',{'form':form})
