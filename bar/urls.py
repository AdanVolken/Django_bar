from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static




from .views import index, bebida

app_name = 'bar'

urlpatterns = [
    path('', index, name= "index" ),
    path('<int:id>', bebida , name= "bebida")
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)