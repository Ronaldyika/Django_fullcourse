# Generated by Django 4.2.1 on 2023-06-24 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerstudent',
            name='studentimage',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='registerteacher',
            name='teacherimage',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
