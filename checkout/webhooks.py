import json
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

import stripe 



@csrf_exempt
def webhook(request):	
	""" Listen for webhooks from stripe """
	wh_secret = settings.STRIPE_WH_SECRET
	stripe.api_key = settings.STRIPE_SECRET_KEY

	payload = request.body
	event = None

	try:
		event = stripe.Event.construct_from(
			json.loads(payload), stripe.api_key
		)
	except ValueError as e:
		# Invalid payload
		return HttpResponse(status=400)
	except stripe.error.SignatureVerificationError as e:
		# Invalid Signature
		return HttpResponse(status=400)
	except Exception as e:
		return HttpResponse(status=400)
	
	handler = StripeWH_Handler(request)
	event_map = {
		'payment_intend.succeeded': handler.handle_payment_intent_succeeded,
		'payment_intend.failed' : handler.handle_payment_intent_succeeded,
	}

	event_type = event['type']
	event_handler = event_map.get(event_type, handler.handle_event)
	response = event_handler(event)

	return response