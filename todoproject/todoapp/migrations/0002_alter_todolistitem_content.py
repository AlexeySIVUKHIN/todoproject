# Generated by Django 4.1.5 on 2023-02-28 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolistitem',
            name='content',
            field=models.TextField(help_text='Введите название задачи', max_length=99),
        ),
    ]
