"""Docstring"""
from django.contrib import admin

from nasarover.models import *


class MineralDetailAdmin(admin.ModelAdmin):
    """Docstring"""
    list_display = ["id", "name"]


class GridDetailAdmin(admin.ModelAdmin):
    """Docstring"""
    list_display = ["id", "x_len", "y_len"]


class SubGridDetailAdmin(admin.ModelAdmin):
    """Docstring"""
    list_display = ["id", "g_id", "pos_x", "pos_y"]


class MineralDisDetailAdmin(admin.ModelAdmin):
    """Docstring"""
    list_display = ["sg_id", "mi_id", "quantity"]


class RoverDetailAdmin(admin.ModelAdmin):
    """Docstring"""
    list_display = ["id", "rover_name"]


class RoverSenDetailAdmin(admin.ModelAdmin):
    """Docstring"""
    list_display = ["id", "r_id", "m_id"]


class RoverPosAdmin(admin.ModelAdmin):
    list_display = ["id", "r_id", "pos_x", "pos_y", "dirn"]

admin.site.register(Mineral, MineralDetailAdmin)
admin.site.register(Grid, GridDetailAdmin)
admin.site.register(SubGrid, SubGridDetailAdmin)
admin.site.register(MineralDis, MineralDisDetailAdmin)
admin.site.register(Rover, RoverDetailAdmin)
admin.site.register(RoverSen, RoverSenDetailAdmin)
admin.site.register(RoverPos, RoverPosAdmin)
