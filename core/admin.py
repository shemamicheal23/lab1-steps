from django.contrib import admin
from core.models import Testing, Transaction, Budget, Category


@admin.register(Testing)
class TestingAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'created_at')

admin.site.register(Transaction)
admin.site.register(Budget)
admin.site.register(Category)
