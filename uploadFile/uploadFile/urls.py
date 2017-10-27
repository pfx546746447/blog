
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve

from disk.views import upload
# from uploadFile.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',upload,name='upload'),

    #url(r'^avatar/(?P<path>.*)/$', serve, {"document_root": MEDIA_ROOT}),

]
