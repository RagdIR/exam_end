from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Users(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1, verbose_name="Пользователи")

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Friends(models.Model):
    friend = models.ManyToManyField(get_user_model(), default="",
                             related_name='add_friend', verbose_name='Пользователь')

    user = models.ForeignKey('webapp.Users', on_delete=models.CASCADE,
                                related_name='friends', verbose_name='Друзья')


    def __str__(self):
        return f'{self.friend.username}'

    class Meta:
        verbose_name = 'Друг'
        verbose_name_plural = 'Друзья'


class Message(models.Model):
    user = models.ForeignKey('webapp.Users',on_delete=models.CASCADE, verbose_name="Пользователь")
    message = models.TextField(("Сообщение"))
    pub_date = models.DateTimeField(verbose_name='Дата сообщения', default=timezone.now)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.message