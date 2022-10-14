# Generated by Django 4.1.1 on 2022-10-03 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('sent_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время ')),
            ],
        ),
    ]
