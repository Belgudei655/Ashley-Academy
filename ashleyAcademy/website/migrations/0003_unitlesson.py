# Generated by Django 4.2.2 on 2023-08-02 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_subject_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='unitLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ytLinks', models.CharField(max_length=100)),
            ],
        ),
    ]
