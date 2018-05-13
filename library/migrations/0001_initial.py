# Generated by Django 2.0.4 on 2018-05-13 15:36

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
            name='BaseLesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='title')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=140, unique=True, verbose_name='slug')),
                ('type', models.CharField(choices=[('0', 'youtube-video'), ('1', 'scrimba-video'), ('2', 'markdown'), ('3', 'quiz'), ('4', 'task')], default='2', max_length=10, verbose_name='type')),
            ],
            options={
                'verbose_name': 'lesson',
                'verbose_name_plural': 'lessons',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='title')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=140, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'module',
                'verbose_name_plural': 'modules',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, default='S', max_length=1000, verbose_name='role')),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='title')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=140, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'track',
                'verbose_name_plural': 'tracks',
            },
        ),
        migrations.CreateModel(
            name='TrackWorkshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library.Track', verbose_name='track')),
            ],
            options={
                'verbose_name': 'track and workshop',
                'verbose_name_plural': 'tracks and workshops',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='title')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=140, unique=True, verbose_name='slug')),
                ('level', models.CharField(choices=[('0', 'beginner'), ('1', 'intermediate'), ('2', 'advanced')], default='0', max_length=10, verbose_name='type')),
                ('last_update_date', models.DateTimeField(auto_now=True, verbose_name='last update date')),
                ('duration', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='duration')),
                ('description', models.CharField(blank=True, max_length=1000, verbose_name='description')),
                ('used_technologies', models.CharField(blank=True, max_length=100, verbose_name='used_technologies')),
                ('workshop_result_url', models.URLField(verbose_name='markdown url')),
                ('authors', models.ManyToManyField(related_name='workshops', to=settings.AUTH_USER_MODEL, verbose_name='authors')),
            ],
            options={
                'verbose_name': 'workshop',
                'verbose_name_plural': 'workshops',
            },
        ),
        migrations.CreateModel(
            name='WorkshopModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library.Module', verbose_name='module')),
                ('workshop', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library.Workshop', verbose_name='workshop')),
            ],
            options={
                'verbose_name': 'workshop and module',
                'verbose_name_plural': 'workshops and modules',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='MarkdownLesson',
            fields=[
                ('baselesson_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.BaseLesson')),
                ('markdown_url', models.URLField(verbose_name='markdown url')),
            ],
            options={
                'abstract': False,
            },
            bases=('library.baselesson',),
        ),
        migrations.CreateModel(
            name='QuizLesson',
            fields=[
                ('baselesson_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.BaseLesson')),
                ('markdown_url', models.URLField(verbose_name='markdown url')),
            ],
            options={
                'abstract': False,
            },
            bases=('library.baselesson',),
        ),
        migrations.CreateModel(
            name='VideoLesson',
            fields=[
                ('baselesson_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.BaseLesson')),
                ('video_url', models.URLField(verbose_name='video url')),
                ('markdown_url', models.URLField(verbose_name='markdown url')),
            ],
            options={
                'abstract': False,
            },
            bases=('library.baselesson',),
        ),
        migrations.AddField(
            model_name='workshop',
            name='modules',
            field=models.ManyToManyField(related_name='workshops', through='library.WorkshopModule', to='library.Module', verbose_name='modules'),
        ),
        migrations.AddField(
            model_name='trackworkshop',
            name='workshop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library.Workshop', verbose_name='workshop'),
        ),
        migrations.AddField(
            model_name='track',
            name='workshops',
            field=models.ManyToManyField(related_name='tracks', through='library.TrackWorkshop', to='library.Workshop', verbose_name='workshops'),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_opened_lesson',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='library.BaseLesson', verbose_name='last opened lesson'),
        ),
        migrations.AddField(
            model_name='profile',
            name='track',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='library.Track', verbose_name='track'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='baselesson',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='lessons', to='library.Module', verbose_name='module'),
        ),
        migrations.AddField(
            model_name='baselesson',
            name='shown_users',
            field=models.ManyToManyField(blank=True, related_name='lessons', to=settings.AUTH_USER_MODEL, verbose_name='shown users'),
        ),
    ]
