from django.http import HttpResponse


class StripeWH_Handler:
    """Handles Stripe webhooks"""
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handles a generic/unexpected/unknown webhook event"""
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """Handles Stripe payment intent succeeded webhook event"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """Handles Stripe payment intent failure webhook event"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
