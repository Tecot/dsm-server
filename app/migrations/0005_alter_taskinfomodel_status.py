# Generated by Django 3.2.15 on 2024-12-11 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20241211_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskinfomodel',
            name='status',
            field=models.IntegerField(choices=[(0, 'success'), (1, 'faild'), (2, 'processing')], default=2, verbose_name='status'),
        ),
    ]
