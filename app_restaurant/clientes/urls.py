from django.urls import path
from . import views

urlpatterns=[
    path('clientes_list/', views.clientes_list, name='clientes_list'),
    path('clientes_details/', views.clientes_details, name='clientes_details'),

    # URLs para las vistas basadas en clases.
    path('clientes_list_vc/', views.ClienteList.as_view(), name='clientes_list_vc'),
    path('clientes_create_vc/', views.ClienteCreate.as_view(), name='clientes_create_vc'),
    path('clientes_edit_vc/<int:pk>/', views.ClienteUpdate.as_view(), name='clientes_edit_vc'),
    path('clientes_delete_vc/<int:pk>/', views.ClienteDelete.as_view(), name='clientes_delete_vc'),

]
