# Generated by Django 4.1.13 on 2024-05-09 03:16

import common.db.encoder
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityLog',
            fields=[
                ('org_id', models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('O', 'Operate log'), ('S', 'Session log'), ('L', 'Login log'), ('T', 'Task')], default=None, max_length=2, null=True, verbose_name='Activity type')),
                ('resource_id', models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Resource')),
                ('datetime', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Datetime')),
                ('detail', models.TextField(blank=True, default='', verbose_name='Detail')),
                ('detail_id', models.CharField(default=None, max_length=36, null=True, verbose_name='Detail ID')),
            ],
            options={
                'verbose_name': 'Activity log',
                'ordering': ('-datetime',),
            },
        ),
        migrations.CreateModel(
            name='FTPLog',
            fields=[
                ('org_id', models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=128, verbose_name='User')),
                ('remote_addr', models.CharField(blank=True, max_length=128, null=True, verbose_name='Remote addr')),
                ('asset', models.CharField(max_length=1024, verbose_name='Asset')),
                ('account', models.CharField(max_length=128, verbose_name='Account')),
                ('operate', models.CharField(choices=[('mkdir', 'Mkdir'), ('rmdir', 'Rmdir'), ('delete', 'Delete'), ('upload', 'Upload'), ('rename', 'Rename'), ('symlink', 'Symlink'), ('download', 'Download'), ('rename_dir', 'Rename dir')], max_length=16, verbose_name='Operate')),
                ('filename', models.CharField(max_length=1024, verbose_name='Filename')),
                ('is_success', models.BooleanField(default=True, verbose_name='Success')),
                ('date_start', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Date start')),
                ('has_file', models.BooleanField(default=False, verbose_name='File')),
                ('session', models.CharField(default=uuid.uuid4, max_length=36, verbose_name='Session')),
            ],
            options={
                'verbose_name': 'File transfer log',
            },
        ),
        migrations.CreateModel(
            name='OperateLog',
            fields=[
                ('org_id', models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=128, verbose_name='User')),
                ('action', models.CharField(choices=[('view', 'View'), ('update', 'Update'), ('delete', 'Delete'), ('create', 'Create'), ('download', 'Download'), ('connect', 'Connect'), ('login', 'Login'), ('change_password', 'Change password'), ('accept', 'Accept'), ('review', 'Review'), ('notice', 'Notifications'), ('reject', 'Reject'), ('approve', 'Approve'), ('close', 'Close')], max_length=16, verbose_name='Action')),
                ('resource_type', models.CharField(max_length=64, verbose_name='Resource Type')),
                ('resource', models.CharField(max_length=128, verbose_name='Resource')),
                ('resource_id', models.CharField(blank=True, db_index=True, default='', max_length=128, verbose_name='Resource')),
                ('remote_addr', models.CharField(blank=True, max_length=128, null=True, verbose_name='Remote addr')),
                ('datetime', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Datetime')),
                ('diff', models.JSONField(default=dict, encoder=common.db.encoder.ModelJSONFieldEncoder, null=True)),
            ],
            options={
                'verbose_name': 'Operate log',
                'ordering': ('-datetime',),
            },
        ),
        migrations.CreateModel(
            name='PasswordChangeLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=128, verbose_name='User')),
                ('change_by', models.CharField(max_length=128, verbose_name='Change by')),
                ('remote_addr', models.CharField(blank=True, max_length=128, null=True, verbose_name='Remote addr')),
                ('datetime', models.DateTimeField(auto_now=True, verbose_name='Datetime')),
            ],
            options={
                'verbose_name': 'Password change log',
            },
        ),
        migrations.CreateModel(
            name='UserLoginLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=128, verbose_name='Username')),
                ('type', models.CharField(choices=[('W', 'Web'), ('T', 'Terminal'), ('U', 'Unknown')], max_length=2, verbose_name='Login type')),
                ('ip', models.GenericIPAddressField(verbose_name='Login IP')),
                ('city', models.CharField(blank=True, max_length=254, null=True, verbose_name='Login city')),
                ('user_agent', models.CharField(blank=True, max_length=254, null=True, verbose_name='User agent')),
                ('mfa', models.SmallIntegerField(choices=[(0, 'Disabled'), (1, 'Enabled'), (2, '-')], default=2, verbose_name='MFA')),
                ('reason', models.CharField(blank=True, default='', max_length=128, verbose_name='Reason')),
                ('status', models.BooleanField(choices=[(1, 'Success'), (0, 'Failed')], default=1, verbose_name='Status')),
                ('datetime', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Login Date')),
                ('backend', models.CharField(default='', max_length=32, verbose_name='Auth backend')),
            ],
            options={
                'verbose_name': 'User login log',
                'ordering': ['-datetime', 'username'],
            },
        ),
        migrations.CreateModel(
            name='UserSession',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('ip', models.GenericIPAddressField(verbose_name='Login IP')),
                ('key', models.CharField(max_length=128, verbose_name='Session key')),
                ('city', models.CharField(blank=True, max_length=254, null=True, verbose_name='Login city')),
                ('user_agent', models.CharField(blank=True, max_length=254, null=True, verbose_name='User agent')),
                ('type', models.CharField(choices=[('W', 'Web'), ('T', 'Terminal'), ('U', 'Unknown')], max_length=2, verbose_name='Login type')),
                ('backend', models.CharField(default='', max_length=32, verbose_name='Auth backend')),
                ('date_created', models.DateTimeField(blank=True, null=True, verbose_name='Date created')),
            ],
            options={
                'verbose_name': 'User session',
                'ordering': ['-date_created'],
                'permissions': [('offline_usersession', 'Offline user session')],
            },
        ),
    ]
