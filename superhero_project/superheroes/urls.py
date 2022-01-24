from django.urls import path

from . import views

app_name = 'superheroes'
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:hero_id>', views.details, name='details'),
  path('new/', views.create, name='create'),
  path('<int:hero_id>/update', views.update, name='update'),
  path('<int:hero_id>/delete', views.delete_hero, name='delete')
  
]