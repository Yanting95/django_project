from django.conf.urls import url
from django.utils import timezone
from django.views.generic import DetailView, ListView
from . models import Kitchen
from . models import Dish
from . forms import KitchenForm, DishForm
from . import views

app_name = 'kitchen'
urlpatterns = [
    url(r'^$', views.kitchen_list, name='kitchen_list'),
    url(r'^kitchens/(?P<pk>\d+)$', views.kitchen_details, name='kitchen_details'),
    url(r'^kitchens/new/$', views.kitchen_new, name='kitchen_new'),
    url(r'^kitchens/(?P<pk>\d+)/dishes$', views.dish_list, name='dish_list'),
    url(r'^kitchens/(?P<pkk>\d+)/dishes/(?P<pk>\d+)$', views.dish_details, name='dish_details'),
    url(r'^kitchens/(?P<pk>\d+)/dishes/new$', views.dish_new, name='dish_new'),
]
