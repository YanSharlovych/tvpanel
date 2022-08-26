import this
import time
from django.shortcuts import render
from .models import order
from datetime import datetime, timedelta, timezone
import requests
from requests.auth import HTTPBasicAuth
import json
from operator import itemgetter, attrgetter

# MonitGlass
def index(request):
    orders = order.objects.all()[:14]

    resttime = datetime.now()

    complete_url = "https://api.openweathermap.org/data/2.5/weather?q=Piatnica&appid=244f6e5b4df1ed3c7873a369acccafb4"
    response = requests.get(complete_url)
    x = response.json()

    y = x["main"]
    icon = x['weather'][0]['icon']

    current_temperature = round(float(y["temp"]) - 273.15)

    if resttime.hour == 21 and resttime.minute >= 3 and resttime.minute < 5:
        endtime_minute = 4
        endtime_second = 60

        timer_m = endtime_minute - datetime.now().minute
        timer_s = endtime_second - datetime.now().second

        if timer_s == 60 and timer_m > 0:
            timer_s = 0
        else:
            timer_s = timer_s

        if timer_s < 10:
            timer_s = "0" + str(timer_s)
        else:
            timer_s = timer_s
        
        if timer_m > 0:
            timer = str(timer_m) + " : " + str(timer_s)
        else:
            timer = str(timer_s)

        rest = "PRZERWA"
        checkrest = True
    else:
        rest = ""
        checkrest = False
        timer = 0
    
    args = {
        'orders': orders,
        'rest' : rest,
        'checkrest' : checkrest,
        'timer' : timer,
        'temperature' : current_temperature,
        'icon' : icon,
        }
        
    return render(request, 'tvpanel/index.html', args)
    
# ZOEX
def test(request):
    # Задаём текущее время
    resttime = datetime.now()

    # Запрос к API
    res = requests.post('https://unispaw.zoex.pl/api/glass/orders/', auth = HTTPBasicAuth('artur', '12345678'))
    
    # Розкодировка
    res_decoded = json.loads(res.text)

    # Убираем ненужные из необработанного списка
    for obj in res_decoded:
        if obj['order_status_name'] != 'Przekazany na produkcje' and obj['order_status_name'] != 'Gotowe do odebrania':
            res_decoded.remove(obj)

    # Обработка даты и перевод её в формат datetime
    for obj in res_decoded:
        x = datetime.strptime(obj['order_datetime'], "%Y-%m-%d %H:%M:%S")
        obj['id'] = int(obj['id'])
        obj['order_datetime'] = (x + timedelta(days=14, hours=12) - datetime.now()).days
        
    # Сортировка объектов
    newlist = sorted(res_decoded, key=lambda d: (d['order_datetime'])) # Первый раз по дате
    newlist = sorted(res_decoded, key=lambda d: (d['order_status_name']), reverse=True) # Второй раз по статусу заказа

    #Убирем ненужные строки из отсортированного списка
    for obj in newlist:
        if obj['order_status_name'] != 'Przekazany na produkcje' and obj['order_status_name'] != 'Gotowe do odebrania':
            newlist.remove(obj)

    # Погода
    complete_url = "https://api.openweathermap.org/data/2.5/weather?q=Piatnica&appid=244f6e5b4df1ed3c7873a369acccafb4"
    response = requests.get(complete_url)
    x = response.json()
    y = x["main"]
    icon = x['weather'][0]['icon']

    current_temperature = round(float(y["temp"]) - 273.15)

    # Модуль перерыва
    if resttime.hour == 12 and resttime.minute >= 0 and resttime.minute < 20:
        endtime_minute = 19
        endtime_second = 60

        timer_m = endtime_minute - datetime.now().minute
        timer_s = endtime_second - datetime.now().second

        if timer_s == 60 and timer_m > 0:
            timer_s = 0
        else:
            timer_s = timer_s

        if timer_s < 10:
            timer_s = "0" + str(timer_s)
        else:
            timer_s = timer_s
        
        if timer_m > 0:
            timer = str(timer_m) + " : " + str(timer_s)
        else:
            timer = str(timer_s)

        
        checkrest = True
    else:
        
        checkrest = False
        timer = 0
    
    # Передаваемые аргументы на страницу
    args = {
        'orders': newlist,
        'checkrest' : checkrest,
        'timer' : timer,
        'temperature' : current_temperature,
        'icon' : icon,
        }
        
    return render(request, 'tvpanel/test.html', args)