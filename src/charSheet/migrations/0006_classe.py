# Generated by Django 4.1.1 on 2022-10-25 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charSheet', '0005_remove_pj_classe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
    ]
