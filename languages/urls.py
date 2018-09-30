from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languages', views.LanguageView)
router.register('programmers', views.ProgrammerView)
router.register('paradigms', views.ParadigmView)

urlpatterns =[
    path('showcase/', include(router.urls)),
]
