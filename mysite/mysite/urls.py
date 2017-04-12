"""mysite URL Configuration

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
from django.conf.urls import url ,include
from django.contrib import admin

urlpatterns = [
	#主应用下的url
    url(r'^admin/', admin.site.urls),
    #将blog中的URL模式包含到项目的主URL模式中,告诉Django在blog/路径下包含了blog应用中的urls.py定义的URL模式。你可以给它们一个命名空间叫做blog，这样你可以方便的引用这个URLs组
    url(r'^blog/', include('blog.urls',
        namespace='blog',
        app_name='blog')),
]
