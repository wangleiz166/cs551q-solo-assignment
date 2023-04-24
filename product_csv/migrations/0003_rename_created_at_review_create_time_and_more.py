# Generated by Django 4.1.2 on 2023-04-15 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_csv', '0002_alter_product_table_alter_review_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='created_at',
            new_name='create_time',
        ),
        migrations.RemoveField(
            model_name='review',
            name='product',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='product_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
