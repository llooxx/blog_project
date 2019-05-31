# Generated by Django 2.2.1 on 2019-05-11 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190507_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='collection_complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '关注的帖子',
                'verbose_name_plural': '关注的帖子',
            },
        ),
        migrations.CreateModel(
            name='collection_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '关注的用户',
                'verbose_name_plural': '关注的用户',
            },
        ),
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30, verbose_name='公司名称')),
                ('company_head', models.CharField(blank=True, max_length=255, null=True, verbose_name='投诉图片')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.category')),
            ],
            options={
                'verbose_name': '公司信息表',
                'verbose_name_plural': '公司信息表',
            },
        ),
        migrations.CreateModel(
            name='hot_complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
            ],
            options={
                'verbose_name': '热门帖',
                'verbose_name_plural': '热门帖',
            },
        ),
        migrations.CreateModel(
            name='hot_news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
            ],
            options={
                'verbose_name': '热门新闻',
                'verbose_name_plural': '热门新闻',
            },
        ),
        migrations.CreateModel(
            name='latest_complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
            ],
            options={
                'verbose_name': '最近发帖',
                'verbose_name_plural': '最近发帖',
            },
        ),
        migrations.CreateModel(
            name='red_black',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(verbose_name='群众打分')),
                ('complaint_amount', models.IntegerField(blank=True, null=True, verbose_name='投诉数量')),
                ('is_red', models.BooleanField(default=False, verbose_name='是否在红榜')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.company')),
            ],
            options={
                'verbose_name': '红黑榜',
                'verbose_name_plural': '红黑榜',
            },
        ),
        migrations.DeleteModel(
            name='Image_test',
        ),
        migrations.RenameField(
            model_name='complaint',
            old_name='page_view_amount',
            new_name='reply_amount',
        ),
        migrations.RenameField(
            model_name='jury',
            old_name='desc',
            new_name='jury_introduce',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='desc',
            new_name='news_introduce',
        ),
        migrations.RemoveField(
            model_name='jury',
            name='occupation',
        ),
        migrations.AddField(
            model_name='comment',
            name='create_time',
            field=models.DateTimeField(auto_now=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='create_time',
            field=models.DateTimeField(auto_now=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='pic',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='投诉图片'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='jury',
            name='create_time',
            field=models.DateTimeField(auto_now=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='jury',
            name='jury_head',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='评审团头像'),
        ),
        migrations.AddField(
            model_name='jury',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='news',
            name='create_time',
            field=models.DateTimeField(auto_now=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='news',
            name='pic',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='新闻图片'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_head',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='用户头像'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='complaint_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.complaint'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=8000, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.user'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.category'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.user'),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(max_length=8000, verbose_name='内容'),
        ),
        migrations.DeleteModel(
            name='Red',
        ),
        migrations.AddField(
            model_name='latest_complaint',
            name='complaint_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.complaint'),
        ),
        migrations.AddField(
            model_name='hot_news',
            name='news_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.news'),
        ),
        migrations.AddField(
            model_name='hot_complaint',
            name='complaint_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.complaint'),
        ),
        migrations.AddField(
            model_name='collection_user',
            name='collected_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='collected_uid', to='blog.user'),
        ),
        migrations.AddField(
            model_name='collection_user',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='uid', to='blog.user'),
        ),
        migrations.AddField(
            model_name='collection_complaint',
            name='collected_complaint_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.complaint'),
        ),
        migrations.AddField(
            model_name='collection_complaint',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.user'),
        ),
    ]
