# Generated by Django 2.1.1 on 2018-10-02 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0006_auto_20181001_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('senha', models.CharField(max_length=255)),
            ],
        ),
    ]