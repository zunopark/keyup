# Generated by Django 2.1.5 on 2019-06-08 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0010_auto_20190608_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dummy_for_histo_and_cloud',
            name='related_keyword_1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dummy_for_histo_and_cloud',
            name='related_keyword_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dummy_for_histo_and_cloud',
            name='related_keyword_3',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dummy_for_histo_and_cloud',
            name='related_keyword_4',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dummy_for_histo_and_cloud',
            name='related_keyword_5',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]