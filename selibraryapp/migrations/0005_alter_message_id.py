# Generated by Django 4.1.1 on 2022-09-15 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selibraryapp', '0004_alter_message_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
