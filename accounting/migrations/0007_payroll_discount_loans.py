# Generated by Django 4.2.7 on 2025-02-05 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0006_alter_payroll_created_at_alter_payroll_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='discount_loans',
            field=models.FloatField(default=0, verbose_name='Descuento por préstamos'),
        ),
    ]
