# Generated by Django 4.1.7 on 2023-03-11 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheme',
            name='name',
            field=models.CharField(default='Scheme', max_length=30),
        ),
    ]