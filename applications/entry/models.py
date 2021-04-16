from datetime import timedelta, datetime

from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy

#THIRD APPS
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

# MANAGERS
from .managers import EntryManager

""" Categories of an entry """

class Category(TimeStampedModel):
    
    short_name = models.CharField(
        'Short name',
        max_length=15,
        unique=True
    )
    name = models.CharField(
        'Name',
        max_length=30
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

""" Tags of an article """

class Tag(TimeStampedModel):

    name = models.CharField(
        'Tag',
        max_length=30
    )

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name

""" Model for entrys or articles """

class Entry(TimeStampedModel):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    tag = models.ManyToManyField(Tag)
    title = models.CharField(
        'Title',
        max_length=200,
    )
    resume = models.TextField('Resume')
    content = RichTextUploadingField('Content')
    public = models.BooleanField(default=False)
    image = models.ImageField(
        'Image',
        upload_to='Entry',
    )
    cover_page = models.BooleanField(default=False)
    in_home = models.BooleanField(default=False)
    slug = models.SlugField(editable=False, max_length=300)

    objects = EntryManager()

    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy(
            'entry_app:entry-detail',
            kwargs={
                'slug': self.slug
            }
        )
    
    # Calculate the seconds total from the curren time
    def save(self, *args, **kwargs):
        now = datetime.now()
        total_time = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds = int(total_time.total_seconds())
        slug_unique = '%s %s' % (self.title, str(seconds))

        self.slug = slugify(slug_unique)

        super(Entry, self).save(*args, **kwargs)