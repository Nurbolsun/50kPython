from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Place(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    views_count = models.IntegerField(default=0)
    is_publicated = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'место'
        verbose_name_plural = 'Места'
        ordering = ['name']

class Feedback(models.Model):
    user = models.ForeignKey(
        to = User,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        verbose_name = 'Пользватель'
    )
    
    place = models.ForeignKey(
        to = Place,
        on_delete = models.CASCADE,
        verbose_name = 'Место'
    )

    text_back = models.TextField(verbose_name='Текст обратной связи')
    
    def __str__(self):
        return self.text_back[:20]
    
    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратные связи'



