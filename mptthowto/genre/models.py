from django.core.urlresolvers import reverse
from django.db import models
from mptt.models import MPTTModel


class Genre(MPTTModel):
    name = models.CharField(max_length=50 , unique=True)
    parent = models.ForeignKey('self' , null=True , blank=True , related_name='children')

    def get_absolute_url(self):
        return reverse('genre_detail', kwargs={'pk': self.pk, })

    class MPTTMeta:
        order_insertion_by = ['name']
