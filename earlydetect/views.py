from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import StressSession
import json
import uuid

@csrf_exempt
def save_questionnaire(request):
    data = json.loads(request.body)
    session_id = str(uuid.uuid4())[:8]
    
    StressSession.objects.create(
        session_id=session_id,
        category=data.get('category', 'other'),
        score=data.get('score', 0),
        percent=float(data.get('score', 0)) / 40 * 100,
        level='low' if float(data.get('score', 0)) / 40 * 100 <= 33 else 'medium' if float(data.get('score', 0)) / 40 * 100 <= 66 else 'high'
    )
    
    return JsonResponse({'success': True, 'session_id': session_id})

@csrf_exempt
def get_dashboard(request):
    sessions = StressSession.objects.all().order_by('-timestamp')[:10]
    return JsonResponse({
        'sessions': [
            {
                'id': s.session_id, 
                'score': s.score, 
                'total': round(s.percent, 1), 
                'level': s.level,
                'category': s.category
            } 
            for s in sessions
        ]
    })
