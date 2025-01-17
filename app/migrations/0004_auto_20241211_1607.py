# Generated by Django 3.2.15 on 2024-12-11 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_taskinfomodel_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskinfomodel',
            name='key',
            field=models.CharField(default='', max_length=64, verbose_name='key'),
        ),
        migrations.AlterField(
            model_name='taskinfomodel',
            name='status',
            field=models.IntegerField(choices=[(0, 'completed'), (1, 'progressing'), (2, 'error')], default=1, verbose_name='status'),
        ),
    ]
