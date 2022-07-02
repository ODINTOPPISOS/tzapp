from django.db import models
from django.utils import timezone

# Создаём модель своего приложения для базы данных
# Create your models here.


class Book(models.Model):
    book_autor = models.CharField('Автор', max_length=50)
    book_janr = models.CharField('Жанр', max_length=50)
    book_izdat = models.CharField('Издатель', max_length=50)
    book_name = models.CharField('Название', max_length=50)
    def __str__(self):
        return self.book_autor

class Bron(models.Model):
    object = models.ForeignKey(Book, on_delete=models.CASCADE)
    bron_status = models.CharField('Забронирована', max_length=50, default='Нет')
    bron_time = models.DateTimeField(default=timezone.now())
    bron_password = models.CharField('Пароль для бронирования', max_length=50, default='')
    bron_login = models.CharField('Логин', max_length=50, default='')
    def __str__(self):
        return self.bron_status