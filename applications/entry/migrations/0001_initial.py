# Generated by Django 3.0.9 on 2021-04-09 23:39

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('short_name', models.CharField(max_length=15, unique=True, verbose_name='Short name')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=30, verbose_name='Tag')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('resume', models.TextField(verbose_name='Resume')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Content')),
                ('public', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='Entry', verbose_name='Image')),
                ('cover_page', models.BooleanField(default=False)),
                ('in_home', models.BooleanField(default=False)),
                ('slug', models.SlugField(editable=False, max_length=300)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entry.Category')),
                ('tag', models.ManyToManyField(to='entry.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Entry',
                'verbose_name_plural': 'Entries',
            },
        ),
    ]
