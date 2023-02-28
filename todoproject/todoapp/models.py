from django.db import models


class TodoListItem(models.Model):
    content = models.CharField(max_length=99, help_text="Введите название задачи")

