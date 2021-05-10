from django.shortcuts import render
from django.apps import apps
from django.urls import reverse


def index(request):
    app_list = [{"name": app.label, "link": reverse(f"{app.label}:index")}
                for app in apps.get_app_configs()
                if not app.name.startswith('django')]
    context = {
        'my_apps': app_list,
    }

    return render(request, 'base.html', context=context)
