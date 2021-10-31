from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view_service/<str:pk>', views.view_service, name='view_service'),
    path('create', views.create, name='create'),
    path('update/<str:pk>', views.update, name='update'),
    path('delete/<str:pk>', views.delete, name='delete')
]
