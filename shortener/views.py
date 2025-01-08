from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from .models import URL
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def shorten_url(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            original_url = data.get('original_url')
            if not original_url:
                return JsonResponse({'error': 'URL طولانی ضروری است.'}, status=400)

            # قبلا انجام شده یا نه
            url_obj, created = URL.objects.get_or_create(original_url=original_url)
            return JsonResponse({'short_url': request.build_absolute_uri('/') + url_obj.short_url}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'فرمت JSON نامعتبر است.'}, status=400)
    else:
        return HttpResponseBadRequest('درخواست باید از نوع POST باشد.')


def redirect_short_url(request, short_url):
    url_obj = get_object_or_404(URL, short_url=short_url)
    return redirect(url_obj.original_url)


def home(request):
    return render(request, 'shortener/home.html')
