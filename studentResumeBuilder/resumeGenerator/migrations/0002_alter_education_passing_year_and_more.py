# Generated by Django 4.1 on 2022-11-14 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeGenerator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='passing_year',
            field=models.TextField(max_length=4),
        ),
        migrations.AlterField(
            model_name='education',
            name='passing_year10',
            field=models.TextField(max_length=4),
        ),
        migrations.AlterField(
            model_name='education',
            name='passing_year12',
            field=models.TextField(max_length=4),
        ),
        migrations.AlterField(
            model_name='resume',
            name='passing_year',
            field=models.TextField(max_length=4),
        ),
        migrations.AlterField(
            model_name='resume',
            name='passing_year10',
            field=models.TextField(max_length=4),
        ),
        migrations.AlterField(
            model_name='resume',
            name='passing_year12',
            field=models.TextField(max_length=4),
        ),
    ]
