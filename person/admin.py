from django.contrib import admin

from person.models import Person, Address


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'is_owner', 'address')
    ordering = ('-created_at',)
    search_fields = ['first_name', 'email', 'last_name']
    actions = ['export_as_csv']
    list_filter = (
        'is_active',
        'is_owner'
    )


class PersonInline(admin.TabularInline):
    model = Person


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'zip_code', 'city', 'state', 'country', 'street')
    ordering = ('-created_at',)
    search_fields = ['zip_code', 'city', 'state', 'country', 'name', 'street']
    actions = ['export_as_csv']
    list_filter = (
        'is_active',
        'city',
        'state',
    )
    inlines = [
        PersonInline
    ]


admin.site.register(Address, AddressAdmin)
admin.site.register(Person, PersonAdmin)
