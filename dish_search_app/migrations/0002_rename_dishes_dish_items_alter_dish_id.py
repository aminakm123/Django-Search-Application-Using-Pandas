# Generated by Django 4.2.2 on 2023-06-28 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dish_search_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='dishes',
            new_name='items',
        ),
        migrations.AlterField(
            model_name='dish',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
