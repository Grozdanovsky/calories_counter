# Generated by Django 4.0.1 on 2022-03-09 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_userfood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfood',
            name='food',
            field=models.ManyToManyField(to='food.Food'),
        ),
    ]
