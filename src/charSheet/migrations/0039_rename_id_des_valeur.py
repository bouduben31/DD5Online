# Generated by Django 4.1.1 on 2022-11-02 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charSheet', '0038_des_proprietearme_type_degat_equipement_poids_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='des',
            old_name='id',
            new_name='valeur',
        ),
    ]
