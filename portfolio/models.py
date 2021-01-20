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

    def __str__(self):
        return self.title

# Algo que va a pasar también una vez que hago cosas con los modelos
# es el migrar a la base de datos, en la consola voy a tener un mensaje de todo lo que tengo que migrar
# se arregla simplemente en la consola con el comando manage.py migrate
# Volvemos a correr el server y ya se fue el mensaje, tener en cuenta cuando trabajamos con models
# cada cambio que querramos hacer tenemos que usar el comando manage.py makemigrations, esto para el modelo que acabamos
# de crear lo tenemos que hacer primero, y lugo cada cambio que querramos hacer, lo manejamos de esa manera
