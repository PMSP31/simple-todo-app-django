# Generated by Django 3.2 on 2022-05-19 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_alter_todo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('VI', 'Very Important'), ('I', 'Important'), ('N', 'Normal')], default='very_important', max_length=50),
        ),
    ]
