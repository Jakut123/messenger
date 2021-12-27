from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (CommentViewSet, CategoryViewSet, ProductViewSet, LikeViewSet, FavoriteViewSet, BasketViewSet, )


router = SimpleRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('comments', CommentViewSet)
router.register('likes', LikeViewSet)
router.register('favorites', FavoriteViewSet)
router.register('basket', BasketViewSet)


urlpatterns = [
    path('', include(router.urls))
]
