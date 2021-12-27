from django.contrib import admin

from products.models import Product, Category, Comment, Like, Favorite, Basket

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Favorite)
admin.site.register(Basket)
