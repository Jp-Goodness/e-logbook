from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    # path('e_logbook/', include('e_logbook.urls')),
]