# Generated by Django 4.1.1 on 2022-09-29 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('image', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_feed', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='likes_feed', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_content', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_reply', to=settings.AUTH_USER_MODEL)),
                ('feed_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feed_reply', to='content.feed')),
            ],
            options={
                'ordering': ['-create_date'],
            },
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_marked', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_bookmark', to=settings.AUTH_USER_MODEL)),
                ('feed_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feed_bookmark', to='content.feed')),
            ],
            options={
                'ordering': ['-create_date'],
            },
        ),
    ]
