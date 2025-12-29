from django.contrib import admin
from .models import UserModel, RoleModel


@admin.register(RoleModel)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("name",)
    filter_horizontal = ("users",)


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email")
