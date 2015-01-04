from django.contrib import admin 
from FitnessApp.models import Users, UserDisabilities, Equipment, EquipmentUsage, EquipmentRepairHistory
# Register your models here.

admin.site.register(Users)
admin.site.register(UserDisabilities)
admin.site.register(Equipment)
admin.site.register(EquipmentUsage)
admin.site.register(EquipmentRepairHistory)
