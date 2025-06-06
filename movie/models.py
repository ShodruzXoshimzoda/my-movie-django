from datetime import date

from django.db import models
from django.urls import reverse

'''     Создание моделей для базы данных '''

class Category(models.Model):
    '''  Категории '''
    name = models.CharField('Категории', max_length=160)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Actor(models.Model):


    name = models.CharField("Имя",max_length=100)
    age = models.PositiveIntegerField("Возраст",default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение",upload_to='actors/',blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актёры и режиссёры"
        verbose_name_plural =  "Актёры и режиссёры"

class Genre(models.Model):
    name = models.CharField('Имя жанра', max_length=160)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Movie(models.Model):
    '''     Фильмы      '''

    title = models.CharField("Название", max_length=160)
    tagline = models.CharField("Слоган", max_length=160,default = "")
    description = models.TextField("Описание")
    poster = models.ImageField("Постер",upload_to='movies/')
    year = models.PositiveSmallIntegerField("Дата выхода", default=2019)
    country = models.CharField("Страна", max_length=50)
    directors = models.ManyToManyField(Actor, verbose_name='режиссёры', related_name='film_director')
    actors = models.ManyToManyField(Actor, verbose_name='актёры',related_name='film_actor')
    genres = models.ManyToManyField(Genre,verbose_name="жанры")
    world_premiere = models.DateField("Премьера в мире", default=date.today)
    budget = models.PositiveIntegerField("Бюджет", default=0,help_text="Указывть сумму в долларах")
    fees_in_usa = models.PositiveIntegerField("Сборы в США",default=0, help_text="Указывть сумму в долларах")
    fess_in_world = models.PositiveIntegerField('Сборы в мире',default=0, help_text="Указывть сумму в долларах")
    category = models.ForeignKey(Category, verbose_name='Категории',on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик",default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        '''  абсолютный url для нашего фильма - один из правильных методов для получения информауии об одном фильме'''
        return reverse('movie_detail', kwargs={'slug':self.url})
    
    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)
    

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class MovieShots(models.Model):
    '''   Кадры из филма '''
    title = models.CharField('Заголовок',max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение",upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадры из фильма"
        verbose_name_plural = "Кадры из фильмлв"


class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField('Значение',default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Звезла рейтинга"
        verbose_name_plural = "Звёзды рейтинга"

class Rating(models.Model):
    ip = models.CharField('IP адресс' ,max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='фильм')

    def __str__(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя",max_length=100)
    text = models.TextField('Сообщение', max_length=5000)
    parent = models.ForeignKey('self',verbose_name='Родитель', on_delete=models.SET_NULL, blank=True,null=True)
    movie = models.ForeignKey(Movie, verbose_name='фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"





