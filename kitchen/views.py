from django.shortcuts import render, redirect, get_object_or_404
from . models import Kitchen, Dish, Days
from . forms import KitchenForm, DishForm, DaysForm
from cart.forms import CartAddForm
from django.contrib.auth.decorators import login_required


def kitchen_list(request):
    kitchens = Kitchen.objects.all()
    return render(request,'kitchen/kitchen_list.html',{'kitchen_list':kitchens})


def kitchen_details(request,pk):
    kitchen = get_object_or_404(Kitchen,pk=pk)
    return render(request,'kitchen/kitchen_detail.html',{'kitchen':kitchen})


@login_required
def kitchen_new(request):
    if request.method == "POST":
        form = KitchenForm(request.POST, request.FILES)
        days_form = DaysForm(request.POST)
        if form.is_valid() and days_form.is_valid():
            work_days = days_form.save()
            kitchen = form.save(commit=False)
            kitchen.days = work_days
            kitchen.save()
            return redirect('kitchen:kitchen_details',pk=kitchen.pk)
    else:
        form = KitchenForm()
        days_form = DaysForm()
    return render(request,'kitchen/kitchen_edit.html',{'form':form, 'days_form':days_form})


def kitchen_update(request,pk):
    kitchen = Kitchen.objects.get(id=pk)
    days = Days.objects.get(id=kitchen.days.id)
    if request.method == "POST":
        form = KitchenForm(request.POST, request.FILES, instance=kitchen)
        days_form = DaysForm(request.POST, instance=days)
        if form.is_valid() and days_form.is_valid():
            work_days = days_form.save()
            kitchen = form.save(commit=False)
            kitchen.days = work_days
            kitchen.save()
            return redirect('kitchen:kitchen_details',pk=kitchen.pk)
    else:
        form = KitchenForm(instance=kitchen)
        days_form = DaysForm(instance=days)
    return render(request,'kitchen/kitchen_edit.html',{'form':form, 'days_form':days_form})


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


@login_required
def dish_new(request,pk):
    if request.method == "POST":
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            dish = form.save(commit=False)
            dish.kitchen = Kitchen.objects.get(id=pk)
            dish.save()
            return redirect('kitchen:dish_details',pkk=dish.kitchen.pk,pk=dish.pk)
    else:
        form = DishForm()
    return render(request,'kitchen/dish_edit.html',{'form':form})


def dish_update(request, pkk, pk):
    dish = get_object_or_404(Dish, id=pk)
    if request.method == "POST":
        form = DishForm(request.POST, request.FILES, instance=dish)
        if form.is_valid():
            dish = form.save(commit=False)
            dish.kitchen = Kitchen.objects.get(id=pkk)
            dish.save()
            return redirect('kitchen:dish_details', pkk=pkk, pk=dish.pk)
    else:
        form = DishForm(instance=dish)
    return render(request, 'kitchen/dish_edit.html', {'form':form})