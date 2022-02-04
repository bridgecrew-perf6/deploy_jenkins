# Generated by Django 3.1.3 on 2022-01-15 00:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0006_productstock'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_1_type', models.CharField(default='SIZE', max_length=10, verbose_name='옵션1 타입')),
                ('option_1_name', models.CharField(blank=True, default='', max_length=50, verbose_name='옵션1 이름(내부용)')),
                ('option_2_type', models.CharField(default='COLOR', max_length=10, verbose_name='옵션2 타입')),
                ('option_2_name', models.CharField(blank=True, default='', max_length=50, verbose_name='옵션2 이름(내부용)')),
                ('option_3_type', models.CharField(blank=True, default='', max_length=10, verbose_name='옵션3 타입')),
                ('option_3_name', models.CharField(blank=True, default='', max_length=50, verbose_name='옵션3 이름(내부용)')),
                ('price', models.IntegerField(default=0)),
                ('count', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='상품')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자')),
            ],
        ),
    ]