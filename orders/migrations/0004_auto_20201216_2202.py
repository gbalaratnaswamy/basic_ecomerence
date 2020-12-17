# Generated by Django 3.1.4 on 2020-12-16 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_orderset'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderset',
            name='is_payment_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderset',
            name='payment_method',
            field=models.CharField(choices=[('CARD', 'CARD'), ('INBK', 'INTERNET BANKING'), ('COD', 'COD')], default='CARD', max_length=20),
        ),
    ]