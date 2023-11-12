from django.shortcuts import render
from .forms import formulario
# Create your views here.

def index(request):
    return render(request, 'Boletin2/index.html')

def crea_formulario(request):
    # Si se ha enviado el formulario
    tablero_form = formulario()
    if request.method == 'POST':
        tablero_form = formulario(request.POST)
        # Ejecutamos la validación
        if tablero_form.is_valid():
            # Los datos se obtienen del diccionario cleaned_data
            username = tablero_form.cleaned_data['username']
            password = tablero_form.cleaned_data['password']
            fechaHora = tablero_form.cleaned_data['fechaHora']
            return render(request, 'Boletin2/index.html',
                          {'username': username, 'password': password,
                           'fechaHora': fechaHora})
    # Si se pide la página por primera vez
    return render(request, 'Boletin2/index.html', {'form': tablero_form})