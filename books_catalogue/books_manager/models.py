from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField('Наименование фильма', max_length=250, blank=True, default='') 
    writer=models.CharField('Имя писателя',max_length=250,blank=True,default='')
    description = models.TextField('Описание', blank=True) 
    created_on = models.DateTimeField('Создано', auto_now_add=True, db_index=True) 
    published_on = models.DateTimeField('Опубликовано', auto_now=True, db_index=True)

    def __str__(self) -> str:
        return f'{self.name}-{self.writer}'
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['-published_on']

