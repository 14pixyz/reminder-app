# Generated by Django 4.2.11 on 2024-10-25 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jusbe', '0002_category_user_remind_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='stripe_card_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='stripe_customer_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='stripe_subscription_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
