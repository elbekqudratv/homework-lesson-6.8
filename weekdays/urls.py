from django.urls import path

from .views import (
    weekdays_ru, weekdays_eng, weekdays_uz,weekdays_list
)


urlpatterns = [
    path('list/', weekdays_list, name='weekdays'),
    path('list/ru/', weekdays_ru, name='weekdays_ru'),
    path('list/eng/', weekdays_eng, name='weekdays_eng'),
    path('list/uz/', weekdays_uz, name='weekdays_uz'),
]