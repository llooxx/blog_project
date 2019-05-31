# Generated by Django 2.2.1 on 2019-05-07 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, default='avatar/demo.png', max_length=200, null=True, upload_to='avatar/%Y/%m', verbose_name='图片测试')),
            ],
            options={
                'verbose_name': '测试图片',
                'verbose_name_plural': '测试图片',
            },
        ),
        migrations.AlterField(
            model_name='complaint',
            name='page_view_amount',
            field=models.IntegerField(blank=True, null=True, verbose_name='浏览量'),
        ),
        migrations.AlterField(
            model_name='red',
            name='complaint_amount',
            field=models.IntegerField(blank=True, null=True, verbose_name='投诉数量'),
        ),
        migrations.AlterField(
            model_name='red',
            name='score',
            field=models.IntegerField(verbose_name='群众打分'),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(verbose_name='年龄'),
        ),
    ]
