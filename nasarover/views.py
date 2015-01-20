"""Docstring"""
from django.shortcuts import redirect, render
from nasarover.forms import GridForm, RoverForm, RoverSenForm
from django.http import HttpResponse
from nasarover.models import Rover, RoverPos
from rest_framework import generics
from nasarover.serializers import RoverSerializer

class RoverList(generics.ListCreateAPIView):
    queryset = Rover.objects.all()
    serializer_class = RoverSerializer
    def get_queryset(self):
        return Rover.objects.filter(user_id = self.request.user)


class RoverDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rover.objects.all()
    serializer_class = RoverSerializer

def index(request):
    """Docstring"""
    if not request.user.is_authenticated():
        return redirect('accounts/login/')
    sform = RoverSenForm()
    if request.method == 'POST':
        form = RoverForm(request.POST)
        if True:
            my_model = form.save()
    else:
        form = RoverForm()
    c = {'form': form, 'sform': sform}
    return render(request, 'index.html', c)


def newgrid(request):
    """Docstring"""
    if not request.user.is_authenticated():
        return redirect('accounts/login/')
    if request.method == 'POST':
        form = GridForm(request.POST)
        if True:
            my_model = form.save()
    else:
        form = GridForm()
    c = {'form': form}
    return render(request, 'grid.html', c)


def senform(request):
    """Docstring"""
    if request.method == 'POST':
        form = RoverSenForm(request.POST)
        if True:
            my_model = form.save()
        return redirect('/')
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')


def process(request):
    """Docstring"""
    if request.method == 'POST':
        r_id = request.POST['rovr']
        r_inst = request.POST['inst']
        grid = request.POST['grid']
        grid_x = request.POST['grid_x']
        grid_y = request.POST['grid_y']
        dirn = request.POST['dirn']
        upd = request.POST.get('upd', False)
        temp_r = Rover.objects.get(id=r_id)
        rovr = RoverPos.objects.filter(id=r_id)
        if len(rovr) < 1:
            rovr = RoverPos(
                g_id=grid, pos_x=grid_x, pos_y=grid_y, r_id=temp_r, dirn=dirn)
            rovr.save()
        if upd:
            rovr_pos = RoverPos.objects.get(id=r_id)
            rovr_pos.g_id = grid
            rovr_pos.pos_x = grid_x
            rovr_pos.pos_y = grid_y
            rovr_pos.r_id = temp_r
            rovr_pos.dirn = dirn
            rovr_pos.save()
        temp_r.process_instruction(r_inst)
        rover_pos = RoverPos.objects.get(id=r_id)
        s = "Final position of rover :  X = " + str(rover_pos.pos_x) + \
            "  Y = " + str(rover_pos.pos_y)\
            + "  Dirn = " + str(rover_pos.dirn)
        return HttpResponse(s)
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')

