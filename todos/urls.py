from django.urls import path
from .views import TodosCreateView, TodosDeleteView

app_name = 'todos'
urlpatterns = [
    path('create/', TodosCreateView.as_view(), name = 'create'),
    path('delete/<int:pk>', TodosDeleteView.as_view(), name = 'delete')
]