from django.contrib import admin

from nasarover.models import *

class MineralDetailAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

class GridDetailAdmin(admin.ModelAdmin):
    list_display = ["id", "x_len", "y_len"]

class SubGridDetailAdmin(admin.ModelAdmin):
    list_display = ["id", "g_id", "pos_x", "pos_y"]

class MineralDisDetailAdmin(admin.ModelAdmin):
    list_display = ["sg_id", "mi_id", "quantity"]

class RoverDetailAdmin(admin.ModelAdmin):
    list_display = ["id", "sg_id", "dirn"]

class RoverSenDetailAdmin(admin.ModelAdmin):
    list_display = ["id", "r_id", "m_id"]

admin.site.register(Mineral,MineralDetailAdmin)
admin.site.register(Grid, GridDetailAdmin)
admin.site.register(SubGrid,SubGridDetailAdmin)
admin.site.register(MineralDis, MineralDisDetailAdmin)
admin.site.register(Rover,RoverDetailAdmin)
admin.site.register(RoverSen, RoverSenDetailAdmin)