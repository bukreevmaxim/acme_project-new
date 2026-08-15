# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import MyUser

# Добавляем поле с биографией 
# к стандартному набору полей (fieldsets) пользователя в панели администратора
UserAdmin.fieldsets += (
    # Добавляем кортеж, где первый элемент — это название раздела в панели администратора,
    # а второй элемент — словарь, где под ключом fields можно указать нужные поля
    ('Extra Fields', {'fields': ('bio',)}),
)
# Регистрируем модель в панели администратора:
admin.site.register(MyUser, UserAdmin)