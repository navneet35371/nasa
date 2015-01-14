from django.shortcuts import *
from forms import GridForm, RoverForm, RoverSenForm
from django.http import HttpResponse
from nasarover.models import *

def index(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    sform = RoverSenForm()
    if request.method == 'POST':
        form = RoverForm(request.POST)
        if form.is_valid():
            # save the model to database, directly from the form:
            my_model = form.save()  # reference to my_model is often not needed at all, a simple form.save() is ok
            # alternatively:
            # my_model = form.save(commit=False)  # create model, but don't save to database
            # my.model.something = whatever  # if I need to do something before saving it
            # my.model.save()
    else:        
        form = RoverForm()
    c = { 'form' : form,'sform' : sform }
    return render(request,'index.html', c)

def newgrid(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    if request.method == 'POST':
        form = GridForm(request.POST)
        if form.is_valid():
            # save the model to database, directly from the form:
            my_model = form.save()  # reference to my_model is often not needed at all, a simple form.save() is ok
            # alternatively:
            # my_model = form.save(commit=False)  # create model, but don't save to database
            # my.model.something = whatever  # if I need to do something before saving it
            # my.model.save()
    else:        
        form = GridForm()
    c = { 'form' : form }
    return render(request,'grid.html', c)

def senform(request):
    if request.method == 'POST':
        form = RoverSenForm(request.POST)
        if form.is_valid():
            my_model = form.save()
        return redirect('/')
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')

def process(request):
    if request.method == 'POST':
        r_id = request.POST['rovr']
        r_inst = request.POST['inst']
        rovr = Rover.objects.get(id = r_id)
        rovr.process_instruction(r_inst)
        return redirect('/')
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')

