# Generated by Django 3.2.2 on 2021-08-23 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reportmeasure',
            options={'ordering': ('report', 'order_num'), 'verbose_name': '报表字段', 'verbose_name_plural': '报表字段'},
        ),
        migrations.AddField(
            model_name='report',
            name='base_queries',
            field=models.TextField(blank=True, default='', verbose_name='基础查询条件'),
        ),
    ]