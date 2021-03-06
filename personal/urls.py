from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.page,name='page'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^personal/',views.location,name="location"),
    url(r'^pick-posts/',views.image_id,name="image_id"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)