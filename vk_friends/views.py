from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.urls import reverse
import vk

from . import urls, utils


# Create your views here.
def index(request):
    """
        index view of vk-friends.
        Returns JSON of available requests
    """
    url = request.build_absolute_uri(reverse(f'{urls.app_name}:cities'))
    context = {
        "message": "Welcome to VK Friends API",
        "available requests": {
            "request 1": {
                "url": f"{url}?user=wannafight",
                "description": "get data of user with vk id 'wannafight'",
            },
            "request 2": {
                "url": f"{url}?user=wannafight&lang=en",
                "description": "get data of user with vk id 'wannafight' "
                               "with English as the response language, "
                               "default: lang=ru",
            },
            "request 3": {
                "url": f"{url}?user=wannafight&lang=ru&forced",
                "description": "get data of user with vk id 'wannafight' "
                               "with forced translation to English",
            },
        }
    }

    return JsonResponse(data=context, status=200,
                        json_dumps_params={'ensure_ascii': False})


def cities(request):
    target = request.GET.get('user', '')
    lang = request.GET.get('lang', 'ru')
    forced = True if 'forced' in request.GET.keys() else False

    response = utils.get_response(target, lang, forced)

    return JsonResponse(data=response,
                        json_dumps_params={'ensure_ascii': False})
