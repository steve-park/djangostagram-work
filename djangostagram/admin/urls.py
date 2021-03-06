"""admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from user.views import Timeline, RegisterUser, LoginUser, logout
from post.views import UploadPost, ViewPost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Timeline.as_view()),
    path('user/register/', RegisterUser.as_view()),
    path('user/login/', LoginUser.as_view()),
    path('user/logout/', logout),
    path('upload/', UploadPost.as_view()),
    path('post/<int:pk>', ViewPost.as_view()),
]
