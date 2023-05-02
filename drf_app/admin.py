from django.contrib import admin

from .models import Actor, Film, ActorFilmWork


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    # Отображение полей в списке
    list_display = ('full_name',)

    # Поиск по полям
    search_fields = ('full_name', 'id')


class PersonFilmWorkInline(admin.TabularInline):
    model = ActorFilmWork
    autocomplete_fields = ['actor', ]


@admin.register(Film)
class FilmWorkAdmin(admin.ModelAdmin):
    inlines = (PersonFilmWorkInline,)

    # Отображение полей в списке
    list_display = ('name', 'type')

    # Фильтрация в списке
    list_filter = ('type',)

    # Поиск по полям
    search_fields = ('title', 'id')
