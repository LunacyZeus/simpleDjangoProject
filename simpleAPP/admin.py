# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from . import models
from simpleDjangoProject.admin import admin_site

class AdminTest(admin.ModelAdmin):
	list_display=('Char字段','时间字段')
	search_fields=('Char字段',)

admin_site.register(models.Test,AdminTest)
#admin_site.register(models.Customer,AdminCustomer)
#admin_site.register(models.ShippingAddress,AdminShippingAddress)