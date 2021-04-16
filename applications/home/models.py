from django.db import models
#
from model_utils.models import TimeStampedModel

""" Model for homepage data """

class Home(TimeStampedModel):
    
    title = models.CharField( 
        'Name',    
        max_length=30
    )
    description = models.TextField()
    about_title = models.CharField(
        'Title us',
        max_length=50
    )
    about_text = models.TextField()
    contact_email = models.EmailField(
        'Contact email',
        blank=True,
        null=True
    )    
    phone = models.CharField(
        'Contact phone',
        max_length=20
    )

    class Meta:
        verbose_name = 'Homepage'
        verbose_name_plural = 'Homepage'

    def __str__(self):
        return self.title

""" Model for subscriptions """

class Subscribers(TimeStampedModel):

    email = models.EmailField()

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        return self.email

""" Contact form """

class Contact(TimeStampedModel):

    full_name = models.CharField(
        'Names',
        max_length=60
    )
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.full_name