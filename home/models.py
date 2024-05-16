from django.db import models

# Create your models here.


class Contact(models.Model):
    sender = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    subject = models.CharField(max_length=254, blank=True, null=True)
    message = models.TextField(blank=False, null=False)
    sent_at = models.DateTimeField(auto_now_add=True)

    # Returns a more readable name for products
    def __str__(self):
        return f'{ self.email } try to contact on the { self.sent_at }'
