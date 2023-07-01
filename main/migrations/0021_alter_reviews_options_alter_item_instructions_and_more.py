# Generated by Django 4.1.3 on 2022-12-14 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20200824_1917'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name': 'Review', 'verbose_name_plural': 'Reviews'},
        ),
        migrations.AlterField(
            model_name='item',
            name='instructions',
            field=models.CharField(default='Available', max_length=250),
        ),
        migrations.AlterField(
            model_name='item',
            name='label_colour',
            field=models.CharField(blank=True, choices=[('danger', 'danger'), ('success', 'success'), ('primary', 'primary'), ('info', 'info'), ('warning', 'warning')], max_length=15),
        ),
        migrations.AlterField(
            model_name='item',
            name='labels',
            field=models.CharField(blank=True, choices=[('Best Selling Foods', 'Best Selling Foods'), ('New Food', 'New Food'), ('Spicy Foods🔥', 'Spicy Foods🔥')], max_length=25),
        ),
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='foods'),
        ),
    ]
