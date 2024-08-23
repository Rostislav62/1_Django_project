"""
URL configuration for my_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.contrib import admin
# from django.urls import path
# from django.contrib.flatpages import views as flatpages_views
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', flatpages_views.flatpage, {'url': '/'}, name='home'),
#     path('about/', flatpages_views.flatpage, {'url': '/about/'}, name='about'),
#     path('page1/', flatpages_views.flatpage, {'url': '/page1/'}, name='page1'),
#     path('page2/', flatpages_views.flatpage, {'url': '/page2/'}, name='page2'),
#     path('admin_only/', flatpages_views.flatpage, {'url': '/admin_only/'}, name='admin_only'),
# ]


from django.contrib import admin
from django.urls import path
from django.contrib.flatpages import views as flatpages_views
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Создание кастомного представления для страницы admin_only
@login_required
def admin_only_view(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("Вы должны быть администратором, чтобы получить доступ к этой странице.")
    return flatpages_views.flatpage(request, url='/admin_only/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', flatpages_views.flatpage, {'url': '/'}, name='home'),
    path('about/', flatpages_views.flatpage, {'url': '/about/'}, name='about'),
    path('page1/', flatpages_views.flatpage, {'url': '/page1/'}, name='page1'),
    path('page2/', flatpages_views.flatpage, {'url': '/page2/'}, name='page2'),
    path('admin_only/', admin_only_view, name='admin_only'),  # Использование кастомного представления
]



