from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from django.urls import include, path

from api.views import (RecipeViewSet, TagViewSet,
                       IngredientViewSet, CustomUserViewSet)

app_name = 'api'

router = DefaultRouter()
router.register('recipes', RecipeViewSet)
router.register('tags', TagViewSet)
router.register('ingredients', IngredientViewSet)
router.register('users', CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

