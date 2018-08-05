from django.conf.urls import include, url
from rest_framework import routers

from .views import Index, ApiNote

router = routers.DefaultRouter()
router.register(r'notes', ApiNote)
app_name = 'note'


urlpatterns = [

    url(r'^$', Index.as_view(), name= 'index'),
    url(r'^ApiNote', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
