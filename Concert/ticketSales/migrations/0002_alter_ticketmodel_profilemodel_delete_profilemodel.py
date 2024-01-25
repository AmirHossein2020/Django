# Generated by Django 4.2.6 on 2024-01-18 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('ticketSales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketmodel',
            name='ProfileModel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.profilemodel', verbose_name='کاربر'),
        ),
        migrations.DeleteModel(
            name='ProfileModel',
        ),
    ]
