# Generated by Django 3.2.5 on 2021-07-20 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20210720_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='result',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='polls.result'),
        ),
    ]