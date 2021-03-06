# Generated by Django 2.1.4 on 2018-12-04 08:31

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atitle', models.CharField(max_length=20)),
                ('aParent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FreshOrder.AreaInfo')),
            ],
            options={
                'db_table': 'AreaInfo',
            },
        ),
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
            ],
            options={
                'db_table': 'CartInfo',
            },
        ),
        migrations.CreateModel(
            name='Gcomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gcomment', tinymce.models.HTMLField()),
            ],
            options={
                'db_table': 'Gcomment',
            },
        ),
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gtitle', models.CharField(max_length=20)),
                ('gprice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('gpic', models.CharField(max_length=200)),
                ('gunit', models.CharField(max_length=8)),
                ('isDelete', models.BooleanField(default=False)),
                ('gdesc', tinymce.models.HTMLField()),
                ('gdetail', tinymce.models.HTMLField()),
            ],
            options={
                'db_table': 'GoodsInfo',
            },
        ),
        migrations.CreateModel(
            name='OrderDetailInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FreshOrder.GoodsInfo')),
            ],
            options={
                'db_table': 'OrderDetailInfo',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otime', models.DateTimeField(auto_now_add=True)),
                ('ototal', models.DecimalField(decimal_places=2, max_digits=8)),
                ('state', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'OrderInfo',
            },
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'TypeInfo',
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=20)),
                ('uaddress', models.CharField(blank=True, max_length=100, null=True)),
                ('uphone', models.CharField(max_length=11)),
                ('ucode', models.CharField(max_length=6)),
                ('ustaue', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'UserAddress',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=50)),
                ('uemail', models.CharField(max_length=40)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'UserInfo',
            },
        ),
        migrations.AddField(
            model_name='useraddress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FreshOrder.UserInfo'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FreshOrder.UserInfo'),
        ),
        migrations.AddField(
            model_name='orderdetailinfo',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FreshOrder.OrderInfo'),
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FreshOrder.TypeInfo'),
        ),
        migrations.AddField(
            model_name='gcomment',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FreshOrder.GoodsInfo'),
        ),
        migrations.AddField(
            model_name='gcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FreshOrder.UserInfo'),
        ),
        migrations.AddField(
            model_name='cartinfo',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FreshOrder.GoodsInfo'),
        ),
        migrations.AddField(
            model_name='cartinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FreshOrder.UserInfo'),
        ),
    ]
