from django.db import models
from django.conf import settings


class Chunk(models.Model):
    """
    A Chunk is a piece of content associated
    with a key that can be inserted into
    any template with the use of a special template
    tag
    """
    key = models.CharField(help_text="name for this chunk of content", blank=False, max_length=50)
    content = models.TextField(blank=True)
    lang = models.CharField(blank=True, null=True, max_length=10, choices=settings.LANGUAGES)

    def __unicode__(self):
        return u"%s" % (self.key,)

    class Meta:
        verbose_name = u'Zones de texte dynamique'