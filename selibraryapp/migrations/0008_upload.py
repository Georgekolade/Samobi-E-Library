# Generated by Django 4.1.1 on 2022-09-19 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selibraryapp', '0007_alter_message_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('file', models.ImageField(default='', upload_to='display')),
            ],
            options={
                'db_table': 'Upload',
            },
        ),
    ]
