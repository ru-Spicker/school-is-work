# Generated by Django 2.1.1 on 2018-09-25 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_mark', models.DateField()),
                ('volume', models.IntegerField()),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_marks.Discipline')),
            ],
        ),
        migrations.CreateModel(
            name='Scholar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('third_name', models.CharField(max_length=50)),
                ('school_number', models.IntegerField()),
                ('class_number', models.CharField(max_length=5)),
                ('date_of_birth', models.DateField(verbose_name='День рождения')),
            ],
        ),
        migrations.AddField(
            model_name='mark',
            name='scholar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_marks.Scholar'),
        ),
    ]
