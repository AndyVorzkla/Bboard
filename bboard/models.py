from django.db import models


class Bb(models.Model):
    # Если не задано значение по умолчанию, то появится значение -----, его можно поменять (None, 'Укажите тип')

    # Перечисление со строковыми(целочисленными models.IntegerChoices) значениями choices=Kinds.choices,
    # default=Kinds.SELL. если тип данных - произвольный, то class ChoicesClass(float, models.Choices)
    class Kinds(models.TextChoices):
        """
        Наследник от enum
        """
        SELL = 's', 'Куплю'
        BUY = 'b', 'Продам'
        EXCHANGE = 'c', 'Обменяю'
        RENT = 'r', 'Напрокат'
        __empty__ = 'Выберите тип публикумого объявления'

    class Measurements(float, models.Choices):
        METERS = 1.0, 'Метры'
        FEET = 0.3048, 'Футы'
        YARDS = 0.9144, 'Ярды'



    KINDS = [
        ('Купля-продажа', (
            ('b', 'Куплю'),
            ('s', 'Продам'),
        )),
        ('Обмен', (
            ('c', 'Обменяю'),
        ))
    ]

    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    # Если доступ к связной модели не требуется, то можно сэкономить ресурс и добавить related_name=+
    # default -> <имя_модели>_set
    rubric = models.ForeignKey(to='Rubric', on_delete=models.PROTECT, verbose_name='Рубрика',
                               related_name='entries', null=True, limit_choices_to={'show': True})
    kind = models.CharField(max_length=1, choices=KINDS, default='s')

    # measurement = models.FloatField(choices=Measurements.choices)
    # db_constraint=True - сохраняет ссылочную целлостность на уровне базы данных, а не только в Django при False
    def __str__(self):
        return f'{self.title}'



    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published', 'title']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')
    show = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return '/bboard/%s/' % self.pk

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ['name']
        get_latest_by = 'published'


class Spare(models.Model):
    name = models.CharField(max_length=30)


class Machine(models.Model):
    name = models.CharField(max_length=100)
    spares = models.ManyToManyField(Spare)
