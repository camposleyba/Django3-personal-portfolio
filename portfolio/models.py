from django.db import models

# Acá estamos creando nuestra clase u objeto que va a ser c/uno de nuestros
# Proyectos que desp se van a ver en la pagina, usamos el models.Model porque
# eso sirve para interactuar con las bases de datos, DJango tiene varias cosas
# pre-construidas para que sea facil para nosotros

class Project(models.Model):

    # Podemos ver todos los tipos que necesitamos usar aca: https://docs.djangoproject.com/en/3.1/ref/models/fields/#field-types
    title = models.CharField(max_length=100) # Charfield, A string field, for small- to large-sized strings.
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/') # Field para imagenes
    url = models.URLField(blank=True) #Blank puede ser agregado a cualquiera de los fields y lo que permite es que exista la posibilidad
                                     #en este caso que tenga URL o no, se puede poner en Title para decidir si se pone o no... etc...
