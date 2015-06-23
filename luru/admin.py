from django.contrib import admin
from luru.models import Department, Gdyear, Dangan

# Register your models here.

class DepatAdmin(admin.ModelAdmin):
	list_display = ('dep_name','tel_num','email')

class DanganAdmin(admin.ModelAdmin):
	list_display = ('gd_name','gd_department','gd_hetong','gd_time','gd_depict')
	list_filter = ('gd_department','gd_time',)
admin.site.register(Department,DepatAdmin)
admin.site.register(Gdyear)
admin.site.register(Dangan,DanganAdmin)