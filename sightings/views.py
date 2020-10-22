from django.shortcuts import render

from .models import Squirrel
from .forms import SquirrelForm
# Create your views here.
def list_of_squirrels(request):
   list_squirrels = Squirrel.objects.all()
   context = {'squirrels': list_squirrels}
   return render(request, 'sightings/list_squirrel.html', context)

def add(request):
       if request.method=='Post':
               form = SquirrelForm(request.POST)
               if form.is_valid():
                       form.save()
                       return redirect(f'/sightings/')
       else:
               form = SquirrelForm()
       context ={
               'form':form
                       }
       return render(request, 'sightings/add.html', context)
