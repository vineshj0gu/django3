"""passwd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from gen import views
from django.conf.urls.static import static
from django.conf import settings
from port import view
from todo import viewt



urlpatterns = [
    path('admin/', admin.site.urls),

    #porfolio

    path('port/',view.home, name='port'),
    path('port1/', include('port.urls')),



    path('blog/', include('blog.urls')),
    path('home/',views.home, name='home'),
    path('time/',views.time, name='time'),

    # passwd gen
    path('home/passwd/',views.passwd, name='pass'),
    path('about/',views.about, name='about'),




    # AUTH
    path('signup/', viewt.signupuser, name='signupuser'),
    path('logout/', viewt.logoutuser, name='logoutuser'),
    path('login/', viewt.loginuser, name='loginuser'),

#todo
    path('current/', viewt.current, name='current'),
    path('alldone/', viewt.alldone, name='alldone'),

    path('todo/<int:todo_pk>', viewt.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', viewt.completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete', viewt.deletetodo, name='deletetodo'),
    path('create/', viewt.create, name='create'),
    path('out/', viewt.out, name='out'),

]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
