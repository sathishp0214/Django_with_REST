"""practice_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from practice_app import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'heroes',views.Heroviewset)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rest_check/',views.api_access),
    url('accounts/', include('django.contrib.auth.urls')),
    url('', include(router.urls)),
    url('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    #used for login and logout (this is seperate for django rest framework)
]
