from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import ProductLineItem, VariantLineItem

# Signal update total is sent when line items are added to order
@receiver(post_save, sender=ProductLineItem)
@receiver(post_save, sender=VariantLineItem)
def update_on_save(sender, instance, created, **kwargs):
	"""
	update order total on lineitems update/create
	"""
	instance.order.update_total()

# Signal update total is sent when line items are deleted from order
@receiver(post_save, sender=ProductLineItem)
@receiver(post_save, sender=VariantLineItem)
def update_on_delete(sender, instance, **kwargs):
	"""
	update order total on lineitems deletion
	"""
	instance.order.update_total()	