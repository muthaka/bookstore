# Generated by Django 4.0.4 on 2022-06-10 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstoreims', '0006_alter_stock_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
