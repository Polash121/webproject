from django.urls import path
from music import views

app_name = 'music'

urlpatterns = [
    path('', views.home, name='home'),
    path('albums/', views.albums, name='albums'),

]