from django.forms import ModelForm
from nasarover.models import Grid, SubGrid, Rover, RoverSen

class GridForm(ModelForm):
    class Meta:
        model = Grid
        fields = '__all__'

class RoverForm(ModelForm):
    class Meta:
        model = Rover
        fields = '__all__'

class RoverSenForm(ModelForm):
    class Meta:
        model = RoverSen
        fields = '__all__'
