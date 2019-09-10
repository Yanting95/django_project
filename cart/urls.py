from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^cart$', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<dish_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<dish_id>\d+)/$', views.cart_remove, name='cart_remove'),
    url(r'^cart/clear$', views.cart_clear, name='cart_clear'),
]
