# Generated by Django 2.1 on 2018-09-27 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_auto_20180927_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço'),
        ),
    ]