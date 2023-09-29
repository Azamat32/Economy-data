# Generated by Django 4.2.4 on 2023-09-29 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_economic_index_path_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='macro_economic_index',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tables', to='api.economic_index'),
        ),
    ]