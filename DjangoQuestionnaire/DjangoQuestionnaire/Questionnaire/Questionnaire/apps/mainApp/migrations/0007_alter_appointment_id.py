# Generated by Django 4.1.5 on 2023-05-15 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_alter_appointment_options_alter_orders_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]