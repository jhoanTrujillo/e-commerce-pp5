from django.contrib import admin
from home.models import Contact

class ContactMessage(admin.ModelAdmin):
	list_display = (
		'sent_at',
		'email',
		'subject',
		'sender',
		'message',
	)

# registers models into admin
admin.site.register(Contact)