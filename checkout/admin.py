from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


"""Displays checkout details for admin"""


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_cart',
                       'stripe_pid')
    fields = ('order_number', 'full_name',
              'email', 'date', 'country',
              'postcode', 'street_address1', 'street_address2',
              'town_or_city', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_cart',
              'stripe_pid')

    list_display = ('order_number', 'full_name', 'date',
                    'order_total', 'delivery_cost', 'grand_total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
