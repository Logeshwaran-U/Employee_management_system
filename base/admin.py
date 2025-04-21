from django.contrib import admin
from . models import Department,PositionList,EmpList
# Register your models here.
admin.site.register(Department)
admin.site.register(PositionList)
admin.site.register(EmpList)