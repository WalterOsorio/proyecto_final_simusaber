from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.bancoPregunta.models import *

@login_required(login_url='/profiles/login')
def read_resultado_view(request):
    resultados=Resultado.objects.all()
    context={
                'resultados':resultados,
            }
    return render(request, "bancoPregunta/readResultados.html",context)