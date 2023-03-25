from django.urls import path
from . import views

urlpatterns = [
    path('', views.homedef),

    path('edicionlimpieza/<codigo>', views.edicionlimpieza),
    path('editarlimpieza/', views.editarlimpieza),
    path('eliminarlimpieza/<codigo>', views.eliminarlimpieza),
]