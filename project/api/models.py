from django.db import models
from django.contrib.auth.models import User


class ChatUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='media/', blank=True)

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Message(models.Model):
    author = models.ForeignKey(ChatUser, on_delete=models.CASCADE)
    room = models.ForeignKey('ChatRoom', on_delete=models.CASCADE, verbose_name="Комната", related_name='message')
    msg = models.TextField(max_length=2000, verbose_name='Сообщение')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f'{self.msg[:32]}'

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class ChatRoom(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название чата')
    author = models.ForeignKey(ChatUser, on_delete=models.CASCADE, related_name='creator', verbose_name='Создатель чата')
    users = models.ManyToManyField(ChatUser, related_name="users", verbose_name="Участники чата", blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"

