# Generated by Django 3.2.15 on 2022-10-18 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0004_auto_20221017_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='edital',
            name='link_resultado',
            field=models.URLField(blank=True, null=True),
        ),
    ]
