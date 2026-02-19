from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import io
import numpy as np
import librosa

# ADD THIS FUNCTION (above)
@csrf_exempt
@require_http_methods(["POST"])
def analyze_questionnaire(request):
    """📋 Questionnaire AI - JSON Response"""
    try:
        # Parse JSON data
        data = json.loads(request.body)
        q_score = data.get('score', 0)
        category = data.get('category', 'other')
        
        # Calculate stress level
        stress_level = 'high' if q_score > 20 else 'medium' if q_score > 10 else 'low'
        percent = (q_score / 40) * 100
        
        # Return PROPER JSON
        return JsonResponse({
            'success': True,
            'questionnaire_stress': stress_level,
            'questionnaire_score': q_score,
            'stress_percent': round(percent, 1),
            'confidence': min(95, 60 + q_score * 2),
            'ai_model': 'PHQ-9 Neural Assessment'
        })
        
    except json.JSONDecodeError:
        # Handle bad JSON
        return JsonResponse({
            'success': False, 
            'error': 'Invalid JSON data'
        }, status=400)
        
    except Exception as e:
        # Handle all other errors
        return JsonResponse({
            'success': False, 
            'error': str(e)
        }, status=500)

    pass

# Your existing functions...
def analyze_voice(request):
    # existing code
    pass

def analyze_face(request):
    # existing code  
    pass
