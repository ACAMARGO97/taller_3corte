from django.urls import path
from apps.libro.views import  listLibros, libroCreate, libroDelete, libroUpdate

app_name= 'libros'
urlpatterns = [
    path('', listLibros, name= 'listlibros'),
    path('nuevo/', libroCreate, name= 'libroCreate'),
    path('actualizar/<int:id_libro>/', libroUpdate, name= 'libroUpdate'),
    path('eeliminar/<int:id_libro>/', libroDelete, name= 'libroDelete'),
]