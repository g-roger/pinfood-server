from django.contrib import admin

from establishment.models import Establishment, Owner
from product.models import Product


class ProductInline(admin.TabularInline):
    model = Product


class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'registration_code', 'is_open', 'is_active', 'created_at')
    ordering = ('-created_at',)
    search_fields = ['name', 'registration_code']
    actions = ['export_as_csv']
    list_filter = (
        'is_active',
        'is_open'
    )
    inlines = [
        ProductInline,
    ]


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'cod_cmvs', 'cod_avcb', 'person', 'establishment', 'created_at', 'is_active')
    ordering = ('-created_at',)
    search_fields = ['cod_cmvs', 'cod_avcb', 'person.name']
    actions = ['export_as_csv']
    list_filter = (
        'is_active',
    )


admin.site.register(Establishment, EstablishmentAdmin)
admin.site.register(Owner, OwnerAdmin)
