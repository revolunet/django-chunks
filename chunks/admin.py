from django.contrib import admin
from models import Chunk


def content_start(obj):
    return u'%s...' % obj.content[:50]
content_start.short_description = 'Contenu'
content_start.allow_tags = False


class ChunkAdmin(admin.ModelAdmin):
    list_display = ('key', 'lang', content_start)
    search_fields = ('key', 'content')

    class Media:
        js = ('js/tiny_mce/tiny_mce.js',
              'js/tiny_config.js',
              )

admin.site.register(Chunk, ChunkAdmin)
