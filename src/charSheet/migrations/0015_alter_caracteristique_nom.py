# Generated by Django 4.1.1 on 2022-10-25 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charSheet', '0014_caracteristique_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caracteristique',
            name='nom',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
