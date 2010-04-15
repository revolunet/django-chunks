from django.contrib import admin
from models import Chunk

class ChunkAdmin(admin.ModelAdmin):
    list_display = ('key',)
    search_fields = ('key', 'content')
    class Media:    # based on MEDIA_URL
        js = ('js/tiny_mce/tiny_mce_src.js',
              'js/tiny_config.js',
              )

admin.site.register(Chunk, ChunkAdmin)