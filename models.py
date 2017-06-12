from django.db import models
from django.utils import timezone

class Organization(models.Model):
    name = models.CharField(verbose_name='Название',max_length=32, unique=True)
    region = models.CharField(verbose_name='Регион',max_length=32, blank=True)
    tax_id = models.PositiveIntegerField(verbose_name='Регистрационный номер')
    site = models.URLField(verbose_name='Сайт',blank=True)

class Work(models.Model):
    organization = models.ForeignKey(Organization, verbose_name='Организация')
    position = models.CharField(verbose_name='Должность', max_length=32)
    duties = models.TextField(verbose_name='Обязанности')
    period = models.PositiveIntegerField(verbose_name='Период')

class Hobby(models.Model):
    name = models.CharField(verbose_name='Название', max_length=32)

class Study(models.Model):
    name = models.CharField(verbose_name='Название', max_length=64)
    date_start = models.DateField(verbose_name='Дата начала обучения')
    date_end = models.DateField(verbose_name='Дата окончания обучения')


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Album(models.Model):
    title = models.CharField("Название альбома", max_length=100)
    slug = models.SlugField("Ссылка для альбома", max_length=100, unique=True)
    img = models.ImageField("Изображение альбома", upload_to='images',
                            help_text='Размер изображения 200px на 200px')

    class Meta:
        ordering = ['title']
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title


class Photo(models.Model):
    title = models.CharField("Название фотографии", max_length=100)
    album = models.ForeignKey(Album, verbose_name='Альбом')
    img = models.ImageField("Фото", upload_to='images',
                            help_text='Желательно, чтоб фото было не большого размера')

    class Meta:
        ordering = ['title']
        verbose_name = 'Фото'
        verbose_name_plural = "Фотографии"

    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title
    def image_thumb(self):
        return '<img src="/media/%s" width="100" height="100" />'  % (self.img)
    image_thumb.allow_tags = True

