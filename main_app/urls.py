from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars_index, name='index'),
    path('cars/<int:car_id>/', views.cars_detail, name='detail'),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
    path('cars/<int:car_id>/add_fueling/', views.add_fueling, name='add_fueling'),
    path('tires/', views.TiresList.as_view(), name='tires_index'),
    path('tires/<int:pk>/', views.TiresDetail.as_view(), name='tires_detail'),
    path('tires/create/', views.TiresCreate.as_view(), name='tires_create'),
    path('tires/<int:pk>/update/', views.TiresUpdate.as_view(), name='tires_update'),
    path('tires/<int:pk>/delete/', views.TiresDelete.as_view(), name='tires_delete'),
    path('cars/<int:car_id>/assoc_tire/<int:tire_id>/', views.assoc_tire, name='assoc_tire'),
]