# Generated by Django 4.1.5 on 2023-05-15 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_medical_orders'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'ordering': ('diagnosys',), 'verbose_name': 'Прийом', 'verbose_name_plural': 'Прийоми'},
        ),
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name': 'Замовлення', 'verbose_name_plural': 'Замовлення'},
        ),
    ]