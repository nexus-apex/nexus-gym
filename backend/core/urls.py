from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('gymmembers/', views.gymmember_list, name='gymmember_list'),
    path('gymmembers/create/', views.gymmember_create, name='gymmember_create'),
    path('gymmembers/<int:pk>/edit/', views.gymmember_edit, name='gymmember_edit'),
    path('gymmembers/<int:pk>/delete/', views.gymmember_delete, name='gymmember_delete'),
    path('fitnessclasses/', views.fitnessclass_list, name='fitnessclass_list'),
    path('fitnessclasses/create/', views.fitnessclass_create, name='fitnessclass_create'),
    path('fitnessclasses/<int:pk>/edit/', views.fitnessclass_edit, name='fitnessclass_edit'),
    path('fitnessclasses/<int:pk>/delete/', views.fitnessclass_delete, name='fitnessclass_delete'),
    path('trainers/', views.trainer_list, name='trainer_list'),
    path('trainers/create/', views.trainer_create, name='trainer_create'),
    path('trainers/<int:pk>/edit/', views.trainer_edit, name='trainer_edit'),
    path('trainers/<int:pk>/delete/', views.trainer_delete, name='trainer_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
