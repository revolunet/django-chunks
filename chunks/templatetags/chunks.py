# -*- encoding: UTF-8 -*-
from django import template
from django.db import models
from django.core.cache import cache
from django.utils import translation

register = template.Library()

Chunk = models.get_model('chunks', 'chunk')
CACHE_PREFIX = "chunk_"


def do_get_chunk(parser, token):
    # split_contents() knows not to split quoted strings.
    tokens = token.split_contents()
    if len(tokens) < 2 or len(tokens) > 3:
        raise template.TemplateSyntaxError, "%r tag should have either 2 or 3 arguments" % (tokens[0],)
    if len(tokens) == 2:
        tag_name, key = tokens
        cache_time = 0
    if len(tokens) == 3:
        tag_name, key, cache_time = tokens
    # Check to see if the key is properly double/single quoted
    if not (key[0] == key[-1] and key[0] in ('"', "'")):
        raise template.TemplateSyntaxError, "%r tag's argument should be in quotes" % tag_name
    # Send key without quotes and caching time
    return ChunkNode(key[1:-1], cache_time)


class ChunkNode(template.Node):
    def __init__(self, key, cache_time=0):
        self.key = key
        self.cache_time = cache_time

    def render(self, context):
        language = translation.get_language()
        try:
            cache_key = CACHE_PREFIX + self.key + language
            c = cache.get(cache_key)
            if c is None:
                c = Chunk.objects.filter(key=self.key, lang__iexact=language)
                if c.count() == 0:
                    c = Chunk.objects.filter(key=self.key)
                c = c[0]
                cache.set(cache_key, c, int(self.cache_time))
            content = c.content
        except (Chunk.DoesNotExist, IndexError):
            content = ''
        return content

register.tag('chunk', do_get_chunk)
