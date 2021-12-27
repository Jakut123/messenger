from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

User = get_user_model()


# def authorized(self, request):
#     if request.method == 'GET':
#         return True
#     return request.user.is_authenticated


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=True, null=True)
    slug = models.SlugField(max_length=30, primary_key=True,)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    category = models.ForeignKey(Category,
                                 on_delete=models.RESTRICT,
                                 related_name='category',
                                 null=True,
                                 blank=True)
    image = models.ImageField(upload_to='products',
                              null=True,
                              blank=True)
    # basket = models.ForeignKey(Basket,
    #                            on_delete=models.RESTRICT,
    #                            related_name='basket',
    #                            )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Comment(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='comments')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments')
    text = models.TextField()
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='likes')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='likes')
    like = models.SmallIntegerField(
        validators=[
            MinValueValidator(-1),
            MaxValueValidator(1)
        ]
    )


# class Korzina(models.Model):
#     author = models.ForeignKey(User,
#                                on_delete=models.CASCADE,
#                                related_name='korzina')
#     product = models.ForeignKey(Product,
#                                 on_delete=models.CASCADE,
#                                 related_name='korzina')
#     korzina = models.CharField(max_length=19, null=True, blank=True)


# class OrderItem(models.Model):
#     order = models.ForeignKey('Order',
#                               on_delete=models.RESTRICT,
#                               related_name='items')
#     product = models.ForeignKey(Product,
#                                 on_delete=models.RESTRICT)
#     quantity = models.SmallIntegerField(default=1)
#
#
# class Order(models.Model):
#     user = models.ForeignKey(User,
#                              on_delete=models.RESTRICT,
#                              related_name='orders')
#     products = models.ManyToManyField(Product, through=OrderItem)
#     created_at = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20)



