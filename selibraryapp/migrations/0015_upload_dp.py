# Generated by Django 4.1.1 on 2022-09-19 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selibraryapp', '0014_alter_upload_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='dp',
            field=models.ImageField(default='pdf.png', upload_to=''),
        ),
    ]
