# Generated by Django 4.2.4 on 2023-08-22 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_contentname_indicatorsname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicatorsname',
            name='link',
            field=models.CharField(max_length=200),
        ),
    ]
