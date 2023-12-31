# Generated by Django 3.1.3 on 2023-07-01 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question_id',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='questions',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='submission',
            old_name='enrollement_id',
            new_name='enrollment',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='choice_text',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='choice_id',
        ),
        migrations.AddField(
            model_name='choice',
            name='text',
            field=models.CharField(default='question text', max_length=550),
        ),
        migrations.AddField(
            model_name='question',
            name='grade',
            field=models.FloatField(default=5.0),
        ),
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.CharField(default='question text', max_length=550),
        ),
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(default='question title', max_length=550),
        ),
        migrations.AddField(
            model_name='submission',
            name='choices',
            field=models.ManyToManyField(to='onlinecourse.Choice'),
        ),
    ]
