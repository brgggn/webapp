from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('diagram_1', views.diagram_1, name='diagram_1'),
    path('diagram_2', views.diagram_2, name='diagram_2'),
    path('diagram_3', views.diagram_3, name='diagram_3'),
    path('diagram_4', views.diagram_4, name='diagram_4'),
    path('diagram_5', views.diagram_5, name='diagram_5'),
    path('diagram_6', views.diagram_6, name='diagram_6'),
]