from django.urls import path
from .views import ElectroListView, ElectroDetailView

urlpatterns = [
    path('', ElectroListView.as_view(), name = 'electro_list'),
    path('<int:pk>', ElectroDetailView.as_view(), name = 'electro_detail'),
    ]