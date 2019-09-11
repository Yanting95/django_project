from django.contrib import admin
from . models import Kitchen
from . models import Dish
from . models import Days

# Register your models here.
admin.site.register(Kitchen)
admin.site.register(Dish)
admin.site.register(Days)
