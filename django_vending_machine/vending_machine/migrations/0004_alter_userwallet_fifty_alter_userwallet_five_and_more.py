# Generated by Django 5.0.4 on 2024-04-07 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vending_machine', '0003_userwallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwallet',
            name='fifty',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userwallet',
            name='five',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userwallet',
            name='hundred',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userwallet',
            name='one',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userwallet',
            name='ten',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userwallet',
            name='twenty',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]