# Generated by Django 3.0.9 on 2021-04-09 23:39

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('full_name', models.CharField(max_length=60, verbose_name='Names')),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=30, verbose_name='Name')),
                ('description', models.TextField()),
                ('about_title', models.CharField(max_length=50, verbose_name='Title us')),
                ('about_text', models.TextField()),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Contact email')),
                ('phone', models.CharField(max_length=20, verbose_name='Contact phone')),
            ],
            options={
                'verbose_name': 'Homepage',
                'verbose_name_plural': 'Homepage',
            },
        ),
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Subscriber',
                'verbose_name_plural': 'Subscribers',
            },
        ),
    ]