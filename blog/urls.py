from django.urls import path
from . import views #Puedo hacer esto porque realmente cree un urls.py yo dentro de la carpeta blogs, asi # QUESTION:
# para importar las views propias puedo hacerlo simplemente con el '.'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
]
