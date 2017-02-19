# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 15:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DegreeAndGrossRecord',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='employee.BaseModel')),
                ('dgr_mark_year', models.CharField(max_length=20)),
                ('dgr_degree', models.CharField(max_length=20)),
                ('dgr_gross', models.CharField(max_length=20)),
            ],
            bases=('employee.basemodel',),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='employee.BaseModel')),
                ('dt_name', models.CharField(max_length=200)),
                ('talk_id', models.CharField(blank=True, max_length=200)),
            ],
            bases=('employee.basemodel',),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='employee.BaseModel')),
                ('real_name', models.CharField(max_length=200)),
                ('work_no', models.CharField(max_length=20)),
                ('talk_user_id', models.CharField(blank=True, max_length=200, null=True)),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('sex', models.SmallIntegerField(choices=[(1, 'boy'), (2, 'girl')], default=1)),
                ('birth', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=256)),
                ('emergent_name', models.CharField(blank=True, max_length=20)),
                ('emergent_mobile', models.CharField(blank=True, max_length=20)),
                ('position', models.CharField(blank=True, max_length=20)),
                ('level', models.CharField(blank=True, max_length=20)),
                ('last_year_degree', models.CharField(blank=True, max_length=20)),
                ('last_year_gross', models.CharField(blank=True, max_length=20)),
                ('emp_related_dt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('employee.basemodel',),
        ),
        migrations.CreateModel(
            name='LevelRecord',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='employee.BaseModel')),
                ('lr_title', models.CharField(max_length=200)),
                ('lr_related_emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
            ],
            bases=('employee.basemodel',),
        ),
        migrations.CreateModel(
            name='PositionRecord',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='employee.BaseModel')),
                ('pr_title', models.CharField(max_length=200)),
                ('pr_related_emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
            ],
            bases=('employee.basemodel',),
        ),
        migrations.CreateModel(
            name='TalkRecord',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='employee.BaseModel')),
                ('tr_title', models.CharField(max_length=200)),
                ('tr_content', models.TextField()),
                ('tr_related_emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
            ],
            bases=('employee.basemodel',),
        ),
    ]