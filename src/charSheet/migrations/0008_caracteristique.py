# Generated by Django 4.1.1 on 2022-10-25 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charSheet', '0007_competence'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caracteristique',
            fields=[
                ('id', models.CharField(max_length=3, primary_key=True, serialize=False)),
            ],
        ),
    ]
