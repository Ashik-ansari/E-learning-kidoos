# Generated by Django 3.2 on 2021-06-11 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin1', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='standard',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin1.myclass'),
        ),
    ]
