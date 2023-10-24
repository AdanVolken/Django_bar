from django.shortcuts import render, get_object_or_404
from .models import Bebida
# Create your views here.
def index(request):
    bebidas = Bebida.objects.all()
    return render(request, 'index.html', {
        "bebidas": bebidas
    })

def bebida(request, id):
    bebida = get_object_or_404(Bebida, id=id)

    return render(request, 'bebida.html', {
        'bebida': bebida
    })