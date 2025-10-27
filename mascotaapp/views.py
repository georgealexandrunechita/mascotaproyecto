from django.http import HttpResponse
from django.shortcuts import render
from .forms import MascotaForm

def miform(request):
    # Manejamos POST y GET
    # Si la petición es POST, recogemos los datos enviados por el formulario y los procesamos
    
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save() # Guardamos la mascota en la base de datos
            return HttpResponse("Mascota guardada")  # Mensaje de confirmación
        
    # Si la petición es GET, mostramos un formulario vacío para que el usuario lo complete
    else:
        form = MascotaForm() # Formulario vacío en GET

    return render(request, "mascotaapp/miform.html", {"form": form})
