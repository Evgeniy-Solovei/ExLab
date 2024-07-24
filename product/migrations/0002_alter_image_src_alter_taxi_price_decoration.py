# Generated by Django 5.0.6 on 2024-07-21 23:35

import django.db.models.deletion
import django.utils.timezone
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='src',
            field=models.ImageField(default='static/image/default.png', upload_to='static/image/', verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='taxi',
            name='price',
            field=models.DecimalField(decimal_places=2, default=Decimal('15.00'), max_digits=10, verbose_name='Цена такси'),
        ),
        migrations.CreateModel(
            name='Decoration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название оформления')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Информация об оформлении')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий к заведению')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно/неактивно')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='decoration_photo', to='product.image', verbose_name='Фото оформления')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='decorations', to='product.service')),
            ],
            options={
                'verbose_name': 'Оформление',
                'verbose_name_plural': 'Оформления',
            },
        ),
    ]