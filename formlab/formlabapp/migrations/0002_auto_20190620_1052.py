# Generated by Django 2.1 on 2019-06-20 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formlabapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='userinfo',
        ),
    ]