# Generated by Django 4.2.2 on 2023-06-21 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0004_alter_address_options_alter_loan_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='status',
            field=models.CharField(blank=True, choices=[('approved', 'Aprovado'), ('denied', 'Negado'), ('pending', 'Pendente')], default='pending', max_length=20, verbose_name='Status da Proposta'),
        ),
    ]
