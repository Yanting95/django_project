from decimal import Decimal
from django.conf import settings
from kitchen.models import Dish


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        dish_ids = self.cart.keys()
        # get the product objects and add them to the cart
        dishes = Dish.objects.filter(id__in=dish_ids)
        for dish in dishes:
            self.cart[str(dish.id)]['dish'] = dish

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def add(self, dish, quantity=1, update_quantity=False):
        dish_id = str(dish.id)
        if dish_id not in self.cart:
            self.cart[dish_id] = {'quantity': 0,
                                  'price': str(dish.price)}
        if update_quantity:
            self.cart[dish_id]['quantity'] = quantity
        else:
            self.cart[dish_id]['quantity'] += quantity
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def clear(self):
        # empty cart
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def get_provider(self):
        for dish_id in self.cart.keys():
            dish = Dish.objects.get(id=dish_id)
        return dish.kitchen
