# Generated by Django 4.1 on 2022-08-24 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvpanel', '0003_alter_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(),
        ),
    ]
