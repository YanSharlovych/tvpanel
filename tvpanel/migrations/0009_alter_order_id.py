# Generated by Django 4.1 on 2022-08-24 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvpanel', '0008_order_id_alter_order_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]