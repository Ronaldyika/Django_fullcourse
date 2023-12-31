# Generated by Django 4.2.1 on 2023-06-24 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assigment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ass', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='RegisterStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentimage', models.ImageField(upload_to='media/')),
                ('studentname', models.CharField(max_length=255)),
                ('matricule', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacherimage', models.ImageField(upload_to='media/')),
                ('teachername', models.CharField(max_length=255, unique=True)),
                ('teacheremail', models.EmailField(max_length=255, unique=True)),
                ('teacherpassword', models.CharField(max_length=40)),
            ],
        ),
    ]
