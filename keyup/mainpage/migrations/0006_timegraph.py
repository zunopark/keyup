# Generated by Django 2.1.5 on 2019-05-30 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_auto_20190531_0335'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeGraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(choices=[('1', '2017 상반기'), ('2', '2017 하반기'), ('3', '2018 상반기'), ('4', '2018 하반기'), ('5', '2019 상반기'), ('6', '2019 하반기')], max_length=2)),
                ('company_name', models.CharField(max_length=100)),
                ('x_axis_keyword', models.CharField(max_length=50)),
                ('y_axis_quantity', models.IntegerField()),
            ],
        ),
    ]