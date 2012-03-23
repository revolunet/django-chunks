from django.contrib import admin
from models import Chunk


class ChunkAdmin(admin.ModelAdmin):
    list_display = ('key', 'lang')
    search_fields = ('key', 'content')

    class Media:
        js = ('js/tiny_mce/tiny_mce.js',
              'js/tiny_config.js',
              )

admin.site.register(Chunk, ChunkAdmin)
