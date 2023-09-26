# Generated by Django 3.2.19 on 2023-08-19 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_year', models.CharField(max_length=8)),
                ('course', models.CharField(max_length=12)),
                ('group', models.CharField(max_length=12)),
                ('arcadian', models.CharField(default=None, max_length=4)),
                ('fname', models.CharField(max_length=12)),
                ('mname', models.CharField(max_length=12)),
                ('lname', models.CharField(max_length=15)),
                ('mother_name', models.CharField(max_length=12)),
                ('inst_code', models.CharField(max_length=15)),
                ('mobile', models.CharField(max_length=12)),
                ('whatsapp', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
    ]