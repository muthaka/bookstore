# Generated by Django 4.0.5 on 2022-06-11 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookstoreims', '0009_alter_stock_book_alter_stock_stock_units'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stock_books', to='bookstoreims.book'),
        ),
    ]