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

import pdb

from django.conf.urls import include, url
from django.contrib import admin
# noinspection PyUnresolvedReferences
from blog.views import index, about, works, learn, post, contact
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^about/$', about, name='about'),
    url(r'^works/$', works, name='works'),
    url(r'^learn/$', learn, name='learn'),
    url(r'^$', pdb.main, name='index'),
    url(r'^post/$', post, name='post'),
    url(r'', include('blog.urls')),
    url(r'^contact/$', contact, name='contact'),
    url(r'^aboyt/index/$',about, name='index'),
    # url(r'^media/(?P<path>*)$','django.vievs.static.server',{'document_root':settings.MEDIA_ROOT},)
    # url(r'^organization/(\d+)/$', organization, name='organization'),
]

# urlpatterns += [
#     url(r'^post/(\d+)/$', post, name='post')
# ]

