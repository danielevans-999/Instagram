from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    url(r'^$',views.home,name='home'),
    url(r'^image/$', views.image_upload,name='upload'),
    url(r'^profile/$', views.profile_info,name='profile'),
    url(r'^edit/$',views.profile_edit,name='edit')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
