# Generated by Django 3.1.1 on 2020-09-24 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_scraps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summary_report',
            name='page_num',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
