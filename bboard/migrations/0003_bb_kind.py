# Generated by Django 4.0.6 on 2022-07-10 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_rubric_alter_bb_options_alter_bb_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='kind',
            field=models.CharField(choices=[('Купля-продажа', (('b', 'Куплю'), ('s', 'Продам'))), ('Обмен', (('c', 'Обменяю'),))], default='s', max_length=1),
        ),
    ]
