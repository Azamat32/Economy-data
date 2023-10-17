# Generated by Django 4.2.4 on 2023-10-17 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_alter_table_macro_economic_index"),
    ]

    operations = [
        migrations.AddField(
            model_name="economic_index",
            name="slug",
            field=models.CharField(max_length=127, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="topic",
            name="slug",
            field=models.CharField(max_length=127, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="table",
            name="macro_economic_index",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="api.economic_index"
            ),
        ),
        migrations.AlterField(
            model_name="topic",
            name="name",
            field=models.CharField(max_length=127, verbose_name="Название разделала"),
        ),
    ]
