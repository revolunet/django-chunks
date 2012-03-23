from django.conf.urls.defaults import *

from django.conf import settings

# statics (for dev only) :
urlpatterns = patterns('',
   (r'imageupload$', 'chunks.admin_views.imageupload'),
   (r'imagelist$', 'chunks.admin_views.imagelist'),
   )

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.CHUNKS_UPLOAD_ROOT}),
    )
