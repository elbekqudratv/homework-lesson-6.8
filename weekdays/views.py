from django.shortcuts import render

# Create your views here.


weekdays = [

    {'name': 'dushanba'},
    {'name': 'seshanba'},
    {'name': 'chorshanba'},
    {'name': 'payshanba'},
    {'name': 'juma'},
    {'name': 'shanba'},
    {'name': 'yakshanba'}
]

weekdays_eng = [

    {'name': 'monday'},
    {'name': 'tuesday'},
    {'name': 'wednesday'},
    {'name': 'Thursday'},
    {'name': 'friday'},
    {'name': 'saturday'},
    {'name': 'sunday'}
]

weekdays_ru = [

    {'name': 'понедельник'},
    {'name': 'вторник'},
    {'name': 'среда'},
    {'name': 'Четверг'},
    {'name': 'пятница'},
    {'name': 'суббота'},
    {'name': 'воскресенье'}
]

weekdays_uz = [

    {'name': 'dushanba'},
    {'name': 'seshanba'},
    {'name': 'chorshanba'},
    {'name': 'payshanba'},
    {'name': 'juma'},
    {'name': 'shanba'},
    {'name': 'yakshanba'}
]


def weekdays_list(request):
    global weekdays
    return  render(request, 'weekdays_list.html', context={'weekdays': weekdays})

def weekdays_eng_list(request):
    global weekdays_eng
    return  render(request, 'weekdays_eng.html', context={'weekdays': weekdays_eng})

def weekdays_ru_list(request):
    global weekdays_ru
    return  render(request, 'weekdays_ru.html', context={'weekdays': weekdays_ru})

def weekdays_uz_list(request):
    global weekdays_uz
    return  render(request, 'weekdays_uz.html', context={'weekdays': weekdays_uz})

