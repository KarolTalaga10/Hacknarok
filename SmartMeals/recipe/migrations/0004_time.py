# Generated by Django 3.1 on 2020-08-29 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_ingredient_owningredient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mins', models.IntegerField()),
            ],
        ),
    ]