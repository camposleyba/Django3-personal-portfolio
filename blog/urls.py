from django.urls import path
from . import views #Puedo hacer esto porque realmente cree un urls.py yo dentro de la carpeta blogs, asi # QUESTION:
# para importar las views propias puedo hacerlo simplemente con el '.'

app_name = 'blog' #ponemos esto porque puede haber una view detail para ambas apps, portfolio y blogs
                  # esto fuerza a que en la parte de URLS tenga que especificar el nombre de la app, para que entienda la ruta

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
