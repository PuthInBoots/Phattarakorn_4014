from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/stores/', views.StoreList.as_view()),
    path('api/stores/<int:store_id>/',
         views.StoreDetailUpdateDelete.as_view(), name='store_detail'),
    path('api/stores/deleteAll/', views.StoreDeleteAll.as_view(),
         name='store_delete_all'),

     path('api/products/', views.ProductList.as_view())
]
