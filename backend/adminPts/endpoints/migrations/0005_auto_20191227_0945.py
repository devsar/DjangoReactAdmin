# Generated by Django 3.0.1 on 2019-12-27 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0004_auto_20191225_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='edad',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='eventos',
            field=models.ManyToManyField(blank=True, null=True, related_name='personas', to='endpoints.evento'),
        ),
    ]