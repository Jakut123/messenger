from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
# from rest_framework.authtoken.admin import User

# Create your models here.


# class Comment(models.Model):
#     name = models.TextField(max_length=10000, null=False, verbose_name='коментарий')
#
#     def __str__(self):
#         return f'{self.name}'
#
#     class Meta:
#         verbose_name = 'коментарий'
#         verbose_name_plural = 'коментарии'


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

    # comment = models.ForeignKey(Comment,
    #                             on_delete=models.CASCADE,
    #                             related_name='comment'
    #                             )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    # author = models.ForeignKey(User,
    #                            on_delete=models.CASCADE,
    #                            related_name='comments')
    text = models.TextField()
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
