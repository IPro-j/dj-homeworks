# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from transliterate import translit
import json
from .leveldb_manager import leveldb_manager


def site(request):
    return render(request, 'site.html')


@api_view(['POST'])
def trans_litter_text(request):
    text = request.data.get('text', '')
    if not text:
        return JsonResponse({'error': 'No text provided'}, status=400)

    try:
        transliterated = translit(text, 'ru', reversed=True)
        return JsonResponse({'transliterated': transliterated})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@api_view(['POST'])
def trans_litter_api(request):
    try:
        if request.content_type != 'application/json':
            return JsonResponse({
                'status': 'error',
                'message': 'Content-Type must be application/json',
                'data': None
            }, status=415)

        try:
            body_data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid JSON in request body',
                'data': None
            }, status=400)

        text = body_data.get('data', '').strip()

        if not text:
            return JsonResponse({
                'status': 'error',
                'message': 'No data provided in "data" field',
                'data': None
            }, status=400)

        # Транслитерация
        transliterated = translit(text, 'ru', reversed=True)

        # Сохранение в LevelDB
        leveldb_manager.save_transliteration(text, transliterated)

        return JsonResponse({
            'status': 'success',
            'data': transliterated
        })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
            'data': None
        }, status=500)


@api_view(['GET'])
def get_history(request):
    try:
        # Получаем параметр n из query parameters, по умолчанию 5
        n = request.query_params.get('n', 5)
        try:
            n = int(n)
            if n < 1:
                n = 5  # Минимальное значение
        except (ValueError, TypeError):
            n = 5  # Если n не число, используем значение по умолчанию

        # Получаем последние N записей из LevelDB
        transliterated_list = leveldb_manager.get_last_n_transliterations(n)

        return JsonResponse({
            'data': transliterated_list
        })
    except Exception as e:
        return JsonResponse({
            'error': str(e)
        }, status=500)
