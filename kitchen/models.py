from django.db import models
from django.urls import reverse

# Create your models here.
# class Days(models.Model):
DAYS_OF_WEEK = (
        ('0', 'Monday'),
        ('1', 'Tuesday'),
        ('2', 'Wednesday'),
        ('3', 'Thursday'),
        ('4', 'Friday'),
        ('5', 'Saturday'),
        ('6', 'Sunday'),
    )
#     day = models.CharField(max_length=8, choices=DAYS_OF_WEEK)


class Kitchen(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    day = models.CharField(max_length=8, choices=DAYS_OF_WEEK)
    # days = models.ManyToManyField(Days)
    start_time = models.TimeField()
    end_time = models.TimeField()
    image = models.ImageField(upload_to="kitchen", blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('kitchen:kitchen_detail', kwargs={'pk': self.pk})


class Dish(models.Model):
    name = models.CharField(max_length=50)
    veg = models.BooleanField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="kitchen", blank=True, null=True)
    kitchen = models.ForeignKey(Kitchen, null=True, related_name='dishes', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('kitchen:dish_detail', kwargs={'pkk': self.kitchen.pk, 'pk': self.pk})
