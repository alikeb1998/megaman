# Generated by Django 3.1.2 on 2020-10-02 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('megapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fish',
            name='last',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
