# Generated by Django 4.0.1 on 2022-03-09 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_alter_foodstatic_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodstatic',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='food.users'),
        ),
    ]
