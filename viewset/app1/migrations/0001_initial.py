# Generated by Django 5.0.2 on 2024-02-07 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('emp_name', models.CharField(max_length=30)),
                ('emp_salary', models.IntegerField()),
                ('emp_designation', models.CharField(max_length=30)),
            ],
        ),
    ]
