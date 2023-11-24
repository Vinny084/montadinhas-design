from django.contrib import admin
from .models import Moto

class MotoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usu')
    list_filter = ('titulo',)
    search_fields = ['titulo']
    exclude = ('usu',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(usu=request.user)
        return qs

    def save_model(self, request, obj, form, change):
        obj.usu = request.user
        return super().save_model(request, obj, form, change)
# Register your models here.
admin.site.register(Moto, MotoAdmin)