from django.shortcuts import render
from .models import Produto


def inicio(request):
    produtos = Produto.objects.filter(disponivel=True)

    return render(
        request,
        'produtos/inicio.html',
        {'produtos': produtos}
    )
