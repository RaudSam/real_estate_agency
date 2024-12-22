from django.contrib import admin

from .models import Flat, Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ['created_at']
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('who_liked',)


class ModelAdmin(admin.ModelAdmin):
    raw_id_fields = ('user_name', 'flat')


admin.site.register(Complaint, ModelAdmin)
admin.site.register(Flat, FlatAdmin)
