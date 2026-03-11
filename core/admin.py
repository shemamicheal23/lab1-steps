from django.contrib import admin
from core.models import Testing


@admin.register(Testing)
class TestingAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'created_at')
