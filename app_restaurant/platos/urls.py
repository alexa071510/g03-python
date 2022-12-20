from django.urls import path
from . import views

urlpatterns=[
    path('platos_list/', views.platos_list, name='platos_list'),
    path('platos_details/', views.platos_details, name='platos_details'),

    # URLs para las vistas basadas en clases.
    path('platos_list_vc/', views.PlatoList.as_view(), name='platos_list_vc'),
    path('platos_create_vc/', views.PlatoCreate.as_view(), name='platos_create_vc'),
    path('platos_edit_vc/<int:pk>/', views.PlatoUpdate.as_view(), name='platos_edit_vc'),
    path('platos_delete_vc/<int:pk>/', views.PlatoDelete.as_view(), name='platos_delete_vc'),

    # URLs serializers
    path('platos_list_serializer/', views.ListPlatoSerializer, name='platos_list_srr'),

]