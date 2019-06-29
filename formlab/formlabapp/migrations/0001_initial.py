# Generated by Django 2.1 on 2019-06-20 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('Email_ID', models.EmailField(max_length=254)),
                ('Mobile_No', models.IntegerField()),
                ('Date_Of_Birth', models.DateField()),
                ('Photo', models.ImageField(upload_to='pic')),
                ('Remark', models.TextField()),
            ],
        ),
    ]
