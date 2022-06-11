# Generated by Django 4.0.5 on 2022-06-11 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookstoreims', '0008_alter_stock_options_remove_stock_books_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_books', to='bookstoreims.book'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stock_units',
            field=models.IntegerField(),
        ),
    ]
