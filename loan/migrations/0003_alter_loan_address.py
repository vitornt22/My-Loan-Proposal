# Generated by Django 3.2.19 on 2023-06-20 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_auto_20230620_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='loan.address', verbose_name='Endereço'),
        ),
    ]