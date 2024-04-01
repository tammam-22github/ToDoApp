from django.urls import path
from . import views

app_name='app1'

urlpatterns = [
    path("",views.Home,name='Home'),
    path("dolist/",views.DoList,name='DoList'),
    path('update/<int:pk>/',views.update_task,name='Update'),
    path("delete/<int:pk>/",views.deletetask,name='Delete'),
    path('create/',views.createtask,name='create'),
    path('detail/<int:pk>/',views.taskdetail,name='detail'),
]

