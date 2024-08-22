from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
    path('admin_only/', views.admin_only, name='admin_only'),
    path('pages/', include('django.contrib.flatpages.urls')),
]

