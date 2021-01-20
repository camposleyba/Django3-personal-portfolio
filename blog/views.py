from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.order_by('-date') #Esta es la manera de poner solamente los mas recientes, con el -date.
                                            # [:5] El brackets puntos 5 es solo para traer 5 elementos de la lista
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id) #Esta es la manera de pasar en la view, el Blog actual, pk es de primary key,
                                               #La funcion get_object_or_404 sirve para ver si encuentra esa key si no, devolvera 404
    return render(request, 'blog/detail.html', {'blog':blog})
