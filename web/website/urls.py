"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView


index_view = TemplateView.as_view(template_name='index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='home'),
    path('about/', index_view, name='about'),
    path('about/team/', index_view, name='team'),
    path('about/history/', index_view, name='history'),
    path('contacts/', index_view, name='contacts'),
    path('contacts/support/', index_view, name='support'),
    path('contacts/feedback/', index_view, name='feedback'),
    path('services/', index_view, name='services'),
    path('services/web/', index_view, name='web_services'),
    path('services/web/design/', index_view, name='web_design'),
    path('services/web/development/', index_view, name='web_development'),
    path('services/mobile/', index_view, name='mobile_services'),
    path('services/mobile/android/', index_view, name='android'),
    path('services/mobile/ios/', index_view, name='ios'),
    path('blog/', index_view, name='blog'),
    path('blog/news/', index_view, name='news'),
    path('blog/tutorials/', index_view, name='tutorials'),
    path('pricing/', index_view, name='pricing'),
    path('pricing/plans/', index_view, name='plans'),
    path('pricing/enterprise/', index_view, name='enterprise'),
]
