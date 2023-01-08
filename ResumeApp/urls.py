from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('add/', views.add, name='add'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('editIns/<int:id>/', views.editIns, name="editIns")
]


urlpatterns += staticfiles_urlpatterns()

