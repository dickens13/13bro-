# Generated by Django 2.0.7 on 2018-07-18 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mod', '0003_auto_20180718_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='chicategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod.ChiCategory', verbose_name='所属分类'),
        ),
    ]
