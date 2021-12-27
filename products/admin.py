from django.contrib import admin

from products.models import Product, Category, Comment, Like

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Like)
