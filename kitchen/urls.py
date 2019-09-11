from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'kitchen'
urlpatterns = [
    url(r'^kitchens$', views.kitchen_list, name='kitchen_list'),
    url(r'^kitchens/(?P<pk>\d+)$', views.kitchen_details, name='kitchen_details'),
    url(r'^kitchens/(?P<pk>\d+)/update$', views.kitchen_update, name='kitchen_update'),
    url(r'^kitchens/new/$', views.kitchen_new, name='kitchen_new'),
    url(r'^kitchens/(?P<pk>\d+)/dishes$', views.dish_list, name='dish_list'),
    url(r'^kitchens/(?P<pkk>\d+)/dishes/(?P<pk>\d+)$', views.dish_details, name='dish_details'),
    url(r'^kitchens/(?P<pkk>\d+)/dishes/(?P<pk>\d+)/update$', views.dish_update, name='dish_update'),
    url(r'^kitchens/(?P<pk>\d+)/dishes/new$', views.dish_new, name='dish_new'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
