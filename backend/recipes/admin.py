from import_export.admin import ImportExportMixin
from users.models import Subscribe, User

from django.contrib import admin

from .models import FavoriteRecipe, Ingredient, Recipe, ShoppingCart, Tag


class IngredientInRecipeInline(admin.TabularInline):
    model = Recipe.ingredients.through


class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInRecipeInline, ]
    list_display = ('id', 'name', 'author', 'added_to_favorites')
    list_filter = ('author', 'name', 'tags')
    empty_value_display = '-пусто-'

    def added_to_favorites(self, obj: Recipe):
        return obj.favorite.count()


class IngredientAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    list_filter = ('name',)


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'password'
    )
    list_filter = ('username', 'email')


class FavoriteRecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'user')


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag)
admin.site.register(User, UserAdmin)
admin.site.register(FavoriteRecipe, FavoriteRecipeAdmin)
admin.site.register(ShoppingCart, FavoriteRecipeAdmin)
admin.site.register(Subscribe)
