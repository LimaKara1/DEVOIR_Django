from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('authentification/', views.authentification, name='authentification'),
    path('rapport/', views.rapport, name='rapport'),
    path('plainte/', views.plainte, name='plainte'),
    path('final/', views.final, name='final'),
    path('bientot/', views.bientot, name='bientot'),
    path('modifier/', views.modifier, name='modifier'),
    path('detail/<int:report_id>/', views.detail, name='detail'),
]

