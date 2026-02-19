from django.urls import path
from . import views

urlpatterns = [
    path('questionnaire/', views.save_questionnaire, name='questionnaire'),
    path('dashboard/', views.get_dashboard, name='dashboard'),
]
