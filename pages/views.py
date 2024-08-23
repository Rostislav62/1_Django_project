from django.shortcuts import render
from pages.contact_info import CONTACT_INFO
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'flatpages/home.html', {
        'title': 'Главная страница',
        'contact_info': CONTACT_INFO
    })

def about(request):
    return render(request, 'flatpages/about.html', {
        'title': 'О нас',
        'contact_info': CONTACT_INFO
    })

def page1(request):
    return render(request, 'flatpages/page1.html', {
        'title': 'Страница 1',
        'contact_info': CONTACT_INFO
    })

def page2(request):
    return render(request, 'flatpages/page2.html', {
        'title': 'Страница 2',
        'contact_info': CONTACT_INFO
    })

@login_required
def admin_only(request):
    return render(request, 'flatpages/admin_only.html', {
        'title': 'Только для Админа',
        'contact_info': CONTACT_INFO
    })

@login_required
def admin_only_view(request):
    return render(request, 'admin_only.html')