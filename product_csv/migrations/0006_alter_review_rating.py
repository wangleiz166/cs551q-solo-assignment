# Generated by Django 4.1.2 on 2023-04-16 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_csv', '0005_alter_review_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.TextField(),
        ),
    ]