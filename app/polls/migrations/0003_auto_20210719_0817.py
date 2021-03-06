# Generated by Django 3.2.5 on 2021-07-19 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_question_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='next_questions',
            field=models.ManyToManyField(null=True, related_name='previous_choices', to='polls.Question'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice_set', to='polls.question'),
        ),
    ]
