# Generated by Django 4.2.2 on 2023-06-26 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chain_store', '0002_store_level_alter_store_debt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=155, verbose_name='Электронная почта')),
                ('country', models.CharField(max_length=155, verbose_name='Страна')),
                ('city', models.CharField(max_length=155, verbose_name='Город')),
                ('street', models.CharField(max_length=155, verbose_name='Улица')),
                ('building_number', models.PositiveIntegerField(verbose_name='Номер здания')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='store',
        ),
        migrations.RemoveField(
            model_name='store',
            name='building_number',
        ),
        migrations.RemoveField(
            model_name='store',
            name='city',
        ),
        migrations.RemoveField(
            model_name='store',
            name='country',
        ),
        migrations.RemoveField(
            model_name='store',
            name='email',
        ),
        migrations.RemoveField(
            model_name='store',
            name='street',
        ),
        migrations.AddField(
            model_name='store',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='chain_store.product', verbose_name='Продукт'),
        ),
        migrations.AddField(
            model_name='store',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chain_store.contact', verbose_name=''),
        ),
    ]