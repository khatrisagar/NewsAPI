# Generated by Django 4.1.2 on 2022-10-15 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsAPI', '0005_alter_news_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]