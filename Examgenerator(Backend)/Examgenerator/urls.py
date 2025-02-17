"""
URL configuration for Examgenerator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.urls import path
from Examapp.views import *

urlpatterns = [

    path('hello',hello),
    path('getAllQuestions/<subject>',getAllQuestions),
    path('getAllSubjects',getAllSubjects),
    path('saveUser',saveUser),
    path('validate',validate),
    path('validate2',validate2),
    path('saveResult',saveResult),
    path('getResults/<subject>',getResults),
    path("getRecordsCounts/<subject>",getRecordsCounts),
    path('getResults2/<subject>/<pageno>',getResults2),
    path('addQuestion',addQuestion),
    path('updateQuestion',updateQuestion),
    path('deleteQuestion/<qno>/<subject>',deleteQuestion),
    path('viewQuestion/<qno>/<subject>',viewQuestion)
    
]