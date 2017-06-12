from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime


def base(request):
    return HttpResponse('index.html'),


def index(request):
    date_example = datetime.date(day=12, month=5, year=2010,)
    post_list = [
        {
            'name': 'Post1',
            'desc': 'Oписание',
            'Date': date_example,
        },
        {
            'name': 'Post2',
            'desc': 'Oписание',
            'Date': date_example,
        },
        {
            'name': 'Post3',
            'desc': 'Oписание',
            'Date': date_example,
        },
    ]
    return render_to_response('index.html'),


def about(request):
    return render_to_response('about.html'),


def post(request):
    return render_to_response('post.html'),


def contact(request):
    return render_to_response('contact.html'),


def main(request):
    name = 'Валентина'
    surname = 'Есикова'
    middlename = 'Михайловна'
    city = 'Оренбург'
    birthday = datetime.date(day=17, month=2, year=1984)
    study = 'Geekbrains.ru'
    info = ['''Начинаю свою карьеру. Хочу работать программистом. Pаботать, разрабатывать проэкты, на Python и 
    Django.''']
    return render_to_response('main.html'),
    # return render_to_response('main.html'['name': name, 'surname': surname, 'middlename': middlename, 'city': city, 'birthday': birthday, 'study': study, 'info': info]),


def works(request):
    page = 'works'
    work_places = [
        {
            'name': 'GeekBrains',
            'post': ' курсы Python, Django',
            'desc': ' '
        },
        {
            'name': ' ...',
            'post': 'Программист',
            'desc': 'Программист (email, телефон, командировки).'
        },
        {
            'name': ' ... ',
            'post': 'Программист-разработчик',
            'desc': ''
        }
    ]
    return render_to_response("works.html", {'page': page, 'work_places': work_places}),


def learn(request):
    page = 'learns'
    learns = [
        {'date_start': datetime.date(year=2008, month=1, day=1),
         'date_end': datetime.date(year=2013, month=1, day=1),
         'place': 'Коледж.'}
    ]
    return render_to_response("learn.html", {'page': page, 'learns': learns}),
