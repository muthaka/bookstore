# Generated by Django 4.0.4 on 2022-06-09 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstoreims', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
