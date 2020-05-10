from django.shortcuts import render


def main_page(request):
    return render(request, 'geosem/main.html', {'title': 'Главная'})


def about_page(request):
    return render(request, 'geosem/about.html', {'title': 'О проекте'})


def map_page(request):
    return render(request, 'geosem/map.html', {'title': 'Карта'})


def info_page(request):
    return render(request, 'geosem/info.html', {'title': 'Информация'})
