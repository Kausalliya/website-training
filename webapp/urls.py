from django.urls import path
from .import views
urlpatterns = [
    path('',views.base,name='base'),
    path('about',views.about,name='about'),
    path('project',views.project,name='project'),
    path('registration',views.registration,name="registration"),
    path('contact',views.contact,name="contact"),
    path('placement',views.placement,name="placement"),






]