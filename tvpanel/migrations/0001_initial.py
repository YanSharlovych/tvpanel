# Generated by Django 4.1 on 2022-08-24 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('order_customer', models.CharField(max_length=200)),
                ('order_complete', models.BooleanField()),
                ('order_count', models.IntegerField()),
                ('order_date', models.DateField()),
            ],
        ),
    ]
