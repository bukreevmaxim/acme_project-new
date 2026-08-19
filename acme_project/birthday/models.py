# birthday/models.py
from django.conf import settings
from django.db import models
from django.urls import reverse

from .validators import real_age


class Tag(models.Model):
    tag = models.CharField('Тег', max_length=20)

    def __str__(self):
        return self.tag

class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия',
        blank=True,
        help_text='Необязательное поле',
            max_length=20
    )
    birthday = models.DateField('Дата рождения', validators=(real_age,))
    image = models.ImageField('Фото', upload_to='birthdays_images/', blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='birthdays',
        verbose_name='Автор записи',
        null=True,
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги',
        blank=True,
        help_text=(
            'Удерживайте Ctrl, а на macOS — Command, '
            'чтобы выбрать несколько вариантов'
        ),
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='unique_birthday_person',
            ),
        )

    def get_absolute_url(self):
        return reverse(
            'birthday:detail',
            kwargs={'pk': self.pk},
        )

class Congratulation(models.Model):
    text = models.TextField('Текст поздравления')
    birthday = models.ForeignKey(
        Birthday,
        on_delete=models.CASCADE,
        related_name='congratulations',
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='congratulations',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)
