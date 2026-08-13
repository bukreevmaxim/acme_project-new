from django.contrib import admin

from .models import Birthday


@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    # Колонки в списке записей
    list_display = ('pk', 'first_name', 'last_name', 'birthday')
    # Поля, по которым можно искать
    search_fields = ('first_name', 'last_name',)
    # Поля для фильтра в правой панели
    list_filter = ('birthday',)