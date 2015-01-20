"""Docstring"""
from django.forms import ModelForm
from nasarover.models import Grid, SubGrid, Rover, RoverSen

class GridForm(ModelForm):
    """Docstring"""
    class Meta:
        """Docstring"""
        model = Grid
        fields = '__all__'

class RoverForm(ModelForm):
    """Docstring"""
    class Meta:
        """Docstring"""
        model = Rover
        fields = '__all__'

class RoverSenForm(ModelForm):
    """Docstring"""
    class Meta:
        """Docstring"""
        model = RoverSen
        fields = '__all__'
