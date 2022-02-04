from django.contrib import admin
from person.models import Person


class PersonAdmin(admin.ModelAdmin):
    def get_address_resume(self, obj):
        return obj.address.state + ' - ' + str(obj.address.zip_code)

    list_display = ('id', 'first_name', 'last_name', 'email', 'is_owner', 'get_address_resume')
    ordering = ('-created_at',)
    search_fields = ['name', 'email', 'last_name']
    actions = ['export_as_csv']
    list_filter = (
        'is_active',
        'is_owner'
    )


admin.site.register(Person, PersonAdmin)
