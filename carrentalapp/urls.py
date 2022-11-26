from django.contrib import admin
from django.urls import path, include
from . import views
from carrent import settings
from django.conf.urls.static import static

urlpatterns = [
    path('kapil', views.DriverFunc, name='kapil'),
    path('bookride', views.BookRide, name='bookride'),
    path('addvehicle', views.AddVehicle, name='addvehicle'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)