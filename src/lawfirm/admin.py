from django.contrib import admin

from lawfirm.models import Account

# Register your models here.


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass
