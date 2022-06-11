from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ownable (models.Model):
    user = models.ForeignKey('auth.User'.verbose_name=_('Author'),
                                related_name="%(class)ss")

class Meta :
    abstract = True

class RegisteredUser (models.Model):
    user = models.OneToOneField(User)
    tracking = models.ManyToManyField('self',related_name='tracked_by',
                                        blank=True,symmetrical=False)

class FeedItem (Ownable):
    content = models.CharField("Content",max_length=1000,
                                    blank=True, null=True)