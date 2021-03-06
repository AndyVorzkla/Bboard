# Generated by Django 4.0.6 on 2022-07-12 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0003_bb_kind'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterModelOptions(
            name='bb',
            options={'ordering': ['-published', 'title'], 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterModelOptions(
            name='rubric',
            options={'get_latest_by': 'published', 'ordering': ['name'], 'verbose_name': 'Рубрика', 'verbose_name_plural': 'Рубрики'},
        ),
        migrations.AddField(
            model_name='rubric',
            name='show',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='bb',
            name='rubric',
            field=models.ForeignKey(limit_choices_to={'show': True}, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='entries', to='bboard.rubric', verbose_name='Рубрика'),
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('spares', models.ManyToManyField(to='bboard.spare')),
            ],
        ),
    ]
