# Generated by Django 2.1 on 2019-06-22 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formlabapp', '0002_auto_20190620_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='Photo',
            field=models.ImageField(upload_to='pict'),
        ),
    ]
