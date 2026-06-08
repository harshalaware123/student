from django.urls import path
from .views import student_view,show,update,delete

urlpatterns = [
    path('add/',student_view),
    path('show/',show,name='show'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),


]