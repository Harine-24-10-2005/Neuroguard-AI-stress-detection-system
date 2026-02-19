from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # Main Flow
    path('', TemplateView.as_view(template_name='stressdetection/index.html'), name='index'),
    path('questionnaire/', TemplateView.as_view(template_name='stressdetection/questionnaire_detection.html'), name='questionnaire'),
    path('voice/', TemplateView.as_view(template_name='stressdetection/voice_detection.html'), name='voice'),
    path('face/', TemplateView.as_view(template_name='stressdetection/face_detection.html'), name='face'),
    path('final/', TemplateView.as_view(template_name='stressdetection/final.html'), name='final'),
    
    # AI Endpoints
    path('questionnaire/analyze/', views.analyze_questionnaire, name='analyze_questionnaire'),
    path('voice/analyze/', views.analyze_voice, name='analyze_voice'),
    path('face/analyze/', views.analyze_face, name='analyze_face'),
]
