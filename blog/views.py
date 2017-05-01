from django.shortcuts import render_to_response
from django.http import HttpResponse, JsonResponse
import datetime
from django.shortcuts import render, get_object_or_404
from django.template import loader


def index(request):
    date_example = datetime.date(day=15, month=5, year=2000)
    post_list =[
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
        }
    ]
    return render_to_response('index.html')


def about(request):
    return render_to_response('about.html')

def post(request):
    return render_to_response('post.html')


def contact(request):
    return render_to_response('contact.html')


# def viewfun(request):
#     return direct_to_template(request, 'index.html', {'num_pages': PAGE_NUM})

# def main(request):
#     name = 'Валентина'
#     surname = 'Есикова'
#     middlename = 'Михайловна'
#     city = 'Оренбург'
#     birthday = datetime.date(day=17,month=2,year=1984)
#     study = ''
# info = [
#     '''Начал свою карьеру в крупной международной компании Prognoz, создавал проекты для правительства РФ в течение 2-х лет.
#     Там познакомился с командной разработкой и системой.
#     После этого работал программистом биллинга на oracle pl/sql в компании "Эр-Телеком Холдинг".
#     Сейчас выполняю свою работу удаленно. С 2014 года стал преподавателем и начал передавать свои знания ученикам.
#     Также не прекращаю работать удаленно и заниматься своими небольшими проектами на Python и Django.'''
#
#     render_to_response_(template_name='index.html'{'name':name, 'surname':surname, 'middlename':middlename, 'city':city, 'birthday':birthday, 'study':study, 'info':info}),
# ]

def works(request):
    page = 'works'
    work_places = [
        {
            'name':'GeekBrains',
            'post':' курсы Python, Django',
            'desc':' '
        },
        {
            'name':' ',
            'post':'Программист',
            'desc':'Программист (email, телефон, командировки).'
        },
        {
            'name':'Прогноз, ЗАО',
            'post':'Программист-разработчик',
            'desc':'Разработка Bi - приложений (Систем сбора, хранения, анализа данных с использованием многомерных структур (типа ADOMD) для органов государственной власти РФ) Формирование регламентной отчетности. Сбор требований у заказчиков (email, телефон, командировки). Консультация заказчиков. Внедрение и поддержка ПО.'
        }
    ]


    return render("works.html",{'page':page, 'work_places':work_places})


def learn(request):
    page = 'learns'
    learns = [
        {'date_start':datetime.date(year=2008, month=1, day=1),'date_end':datetime.date(year=2013, month=1, day=1),'place':'Пермский государственный национальный исследовательский университет'}
    ]
    return render("learn.html",{'page':page, 'learns':learns})

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)



def organization(request, id, Organization=None):
    page = 'organization'
    '''
    try:
        org = Organization.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404
    '''
    org = get_object_or_404(Organization,id=id)
    return render_to_response('organization.html',{'organization':org})



def get_works(request, Work=None):
    if request.is_ajax():
        slice = request.POST['slice']
        work_places = Work.objects.all().order_by('organization__name')
        if slice:
            work_places = work_places[:int(slice)]
        html = loader.render_to_string('inc-place_works.html', {'work_places':work_places})
        data = {'html':html}
        return JsonResponse(data)
