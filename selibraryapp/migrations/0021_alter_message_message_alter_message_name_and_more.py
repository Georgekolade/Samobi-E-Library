# Generated by Django 4.1.2 on 2022-10-29 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selibraryapp', '0020_alter_upload_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='message',
            name='subject',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='upload',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
