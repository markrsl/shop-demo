# Generated by Django 3.2.9 on 2021-11-25 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
                ('intro', models.TextField()),
                ('inventory', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.PositiveIntegerField()),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('consumer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.consumer')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.item')),
            ],
        ),
    ]