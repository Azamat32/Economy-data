# Generated by Django 4.2.4 on 2023-09-08 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название разделала')),
            ],
        ),
        migrations.CreateModel(
            name='Economic_index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('path', models.CharField(max_length=255, null=True)),
                ('macro_topic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.topic')),
            ],
        ),
    ]
