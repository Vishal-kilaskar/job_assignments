from django.shortcuts import render
from .models import Movies
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'movie_data/home.html')


def get_data(request):
    if request.method == 'GET':
        all_data = Movies.objects.all().values()
        return JsonResponse(list(all_data), safe=False)
    else:
        return JsonResponse({})

@csrf_exempt
def post_data(request):
    to_update = json.loads(request.body)
    obj_inst = Movies.objects.get(pk=to_update['id'])
    obj_inst.movie_upvotes = to_update['movie_upvotes']
    obj_inst.save()
    return JsonResponse({'success': True})
