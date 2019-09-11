from django.core.mail import send_mass_mail
from .models import Order
from kitchen.models import Kitchen
from feast_freedom.settings import EMAIL_FROM


def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Confirmation of Order no. {}'.format(order.id)
    message_user = 'Dear {},\n\nYou have successfully placed an order. Your order id is {}.'.format(order.user.first_name,
                                                                             order.id)
    message_kitchen = 'Dear {},\n\nYou have received an order. The order id is {}.'.format(order.provider.name,
                                                                                               order.id)
    message1 = (subject, message_user, EMAIL_FROM, [order.user.email])
    kitchen = Kitchen.objects.get(id=order.provider_id)
    message2 = (subject, message_kitchen, EMAIL_FROM, [kitchen.email])
    mail_sent = send_mass_mail((message1, message2), fail_silently=False)
    # mail_sent = send_mail(subject, message, 'admin@myshop.com', [order.email])
    # mail_sent = send_mail(subject, message_kitchen, 'admin@myshop.com', [order.kitchen.email])
    return mail_sent

