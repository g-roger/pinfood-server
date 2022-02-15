from django.contrib import admin

from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'unit_price', 'quantity', 'date_available', 'date_limit', 'is_active',
                    'establishment')
    ordering = ('-created_at',)
    search_fields = ['name', 'establishment__name']
    actions = ['export_as_csv']
    list_filter = (
        'is_active', 'unit_price'
    )


admin.site.register(Product, ProductAdmin)
