# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin
# Register your models here.

class MyAdminSite(admin.AdminSite):
    site_header = '后台管理'

admin_site = MyAdminSite()

admin_site.register(User,UserAdmin)
admin_site.register(Group,GroupAdmin)
