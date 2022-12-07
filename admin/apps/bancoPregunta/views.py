# from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.http import HttpResponse
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, F
from django.db.models import Value as V
from django.db.models.functions import Concat
from django.contrib.auth.forms import AuthenticationForm
from apps.profiles.form import *
from apps.prueba.models import Grado
from apps.bancoPregunta.models import *

@login_required(login_url='/profiles/login')
def read_resultado_view(request):
    resultados=Resultado.objects.all()
    context={
                'resultados':resultados,
            }
    return render(request, "bancoPregunta/readResultados.html",context)

def create_pregunta_view(request):
    grados = Grado.objects.all()
    materias = Materia.objects.all()
    estados = Estado.objects.all()
    
    return render(request, 'bancoPregunta/createPregunta.html')
    
    