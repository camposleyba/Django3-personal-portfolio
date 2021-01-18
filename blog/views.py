from django.shortcuts import render
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')[:5] #Esta es la manera de poner solamente los mas recientes, con el -date.
                                            # El brackets puntos 5 es solo para traer 5 elementos de la lista
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})
