from django.urls import path, include
from .views import ListTodo, DetailTodo
# DateilTodoインスタンスですべてのデータを取りに行っている。
urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()),
    path('', ListTodo.as_view())
]