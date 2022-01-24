from warnings import catch_warnings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Superhero

# Create your views here.
def index(request):
  all_heroes = Superhero.objects.all()
  context = {
    'all_heroes': all_heroes
  }
  return render(request, 'superheroes/index.html', context)

def details(request, hero_id):
  single_hero = Superhero.objects.get(pk=hero_id)
  context = {
    'hero': single_hero
  }
  return render(request, 'superheroes/details.html', context)

def create(request):
  if request.method == "POST":
    #save the form as a new db content
    #return to index
    name = request.POST.get('name')
    alter_ego = request.POST.get('alter_ego')
    primary = request.POST.get('primary')        
    secondary = request.POST.get('secondary')
    catchphrase = request.POST.get('catchphrase')
   
    new_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary, secondary_ability=secondary, catch_phrase=catchphrase)
    new_hero.save()
    return HttpResponseRedirect(reverse('superheroes:index'))

  else:
    return render(request, 'superheroes/create.html')


def update(request, hero_id):
  update_hero = Superhero.objects.get(pk=hero_id)
  context = {
      'hero' : update_hero
  }

  if request.method == "POST":
    update_hero.name = request.POST.get('name')
    update_hero.alter_ego = request.POST.get('alter_ego')
    update_hero.primary_ability = request.POST.get('primary')        
    update_hero.secondary_ability = request.POST.get('secondary')
    update_hero.catch_phrase = request.POST.get('catchphrase')
    
    # update_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary, secondary_ability=secondary, catch_phrase=catchphrase)
    update_hero.save()
    
    return HttpResponseRedirect(reverse('superheroes:index'))

  else:
    return render(request, 'superheroes/update.html', context)
    


def delete_hero(request, hero_id):
  single_hero = Superhero.objects.get(pk=hero_id)
  # context = {
  #   'hero': single_hero
  # }
  # if request.method == 'POST':
  single_hero.delete()

  return HttpResponseRedirect(reverse('superheroes:index'))
  # else:
  #   return render(request, 'superheroes/details.html', context)