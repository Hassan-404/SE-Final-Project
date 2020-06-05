from django.contrib import admin
from .models import croplist, cropdetail, fertilizerdetail, diseasedetail, pesticidedetail, UserCrop, City
# Register your models here.

admin.site.register(croplist)
admin.site.register(cropdetail)
admin.site.register(fertilizerdetail)
admin.site.register(diseasedetail)
admin.site.register(pesticidedetail)
admin.site.register(UserCrop)
admin.site.register(City)
