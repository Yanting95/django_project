from django.conf.urls import url
from . import views

app_name = 'orders'
urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^order/$', views.order_list, name='order_list'),
    url(r'^order/(?P<order_id>\d+)$', views.order_detail, name='order_detail')
]
