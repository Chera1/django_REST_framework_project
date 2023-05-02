from django.db import models


class TypeFilm(models.TextChoices):
    """Наследуемый класс от TextChoices, позволяющий в поле установить выбор из перечисленных данных."""

    movie = 'MOVIE', 'фильм'
    tv_show = 'TV_SHOW', 'шоу'


class TypeRole(models.TextChoices):
    """Наследуемый класс от TextChoices, позволяющий в поле установить выбор из перечисленных данных."""

    actor = 'actor', 'актер'
    director = 'director', 'режиссер'
    writer = 'writer', 'сценарист'


class Film(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    type = models.CharField(verbose_name='type', choices=TypeFilm.choices, max_length=100)

    class Meta:
        # Следующие два поля отвечают за название модели в интерфейсе
        verbose_name = 'Кинопроизведение'
        verbose_name_plural = 'Кинопроизведения'

    def __str__(self):
        return self.name


class Actor(models.Model):
    full_name = models.TextField(null=True, db_index=True)
    age = models.IntegerField(null=True)

    class Meta:
        # Следующие два поля отвечают за название модели в интерфейсе
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'

    def __str__(self):
        return self.full_name


class ActorFilmWork(models.Model):
    films = models.ForeignKey(Film, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    role = models.CharField('role', null=True, choices=TypeRole.choices, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
