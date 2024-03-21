# Generated by Django 4.2.11 on 2024-03-18 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='function',
            field=models.CharField(choices=[('Manager', 'Manager'), ('Supervisor', 'Supervisor'), ('Seller', 'Seller')], default='Seller', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='seller',
            name='seller_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]