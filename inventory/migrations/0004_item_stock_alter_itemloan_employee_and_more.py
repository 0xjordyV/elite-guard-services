# Generated by Django 4.2.7 on 2025-01-21 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0017_remove_employee_service'),
        ('services', '0010_alter_service_location'),
        ('inventory', '0003_alter_item_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='stock',
            field=models.PositiveIntegerField(default=0, verbose_name='Cantidad en inventario'),
        ),
        migrations.AlterField(
            model_name='itemloan',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee', verbose_name='Empleado'),
        ),
        migrations.AlterField(
            model_name='itemloan',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.item', verbose_name='Artículo'),
        ),
        migrations.AlterField(
            model_name='itemloan',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service', verbose_name='Servicio'),
        ),
        migrations.DeleteModel(
            name='ItemStock',
        ),
    ]
