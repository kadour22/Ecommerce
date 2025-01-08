# Generated by Django 4.2 on 2025-01-06 13:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CartItems', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default=uuid.uuid4, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cartitems', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='CartItems.cartitems')),
            ],
        ),
    ]
