# Generated by Django 4.1.2 on 2023-04-05 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cart',
            table='cart',
        ),
        migrations.AlterModelTable(
            name='order',
            table='order',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
