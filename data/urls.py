from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list_create, name='crear'),
    path('<str:uniqueID>', views.product_detail_view, name='detail')
]