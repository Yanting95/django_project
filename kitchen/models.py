from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Days(models.Model):
    Monday = models.BooleanField()
    Tuesday = models.BooleanField()
    Wednesday = models.BooleanField()
    Thursday = models.BooleanField()
    Friday = models.BooleanField()
    Saturday = models.BooleanField()
    Sunday = models.BooleanField()



class Kitchen(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    # day = models.CharField(max_length=8, choices=DAYS_OF_WEEK)
    days = models.ForeignKey(Days, related_name='days', on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    image = models.ImageField(upload_to="kitchen/", blank=True, null=True)
    user = models.ForeignKey(User, related_name='kitchen_user', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('kitchen:kitchen_detail', kwargs={'pk': self.pk})


class Dish(models.Model):
    name = models.CharField(max_length=50)
    veg = models.BooleanField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="dish/", blank=True, null=True)
    kitchen = models.ForeignKey(Kitchen, null=True, related_name='dishes', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('kitchen:dish_detail', kwargs={'pkk': self.kitchen.pk, 'pk': self.pk})


