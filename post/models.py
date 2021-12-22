from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'тэг'
        verbose_name_plural = 'тэги'


class Post(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    tag = models.ForeignKey(Tag,
                            on_delete=models.CASCADE,
                            related_name='tag'
                            )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'



