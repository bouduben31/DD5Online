# Generated by Django 4.1.1 on 2022-10-23 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charSheet', '0003_alter_character_classe'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='proficiencies',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
