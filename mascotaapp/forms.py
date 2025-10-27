from django import forms
from .models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = "__all__"
        # Renombramos los atributos del modelo para mostrar etiquetas más amigables en el formulario
        labels = {
            "nombre": "Nombre",
            "raza": "Raza",
            "fecha_nacimiento": "Fecha de nacimiento",
            "peso": "Peso en kilos",
            "vacunado": "Vacunado",
            "ultima_vacuna": "Fecha de la última vacuna",
            "email_duenyo": "Email del dueño",
            "domicilio_duenyo": "Domicilio del dueño"
        }
        # Widgets para campos de fecha
        widgets = {
            "fecha_nacimiento": forms.DateInput(attrs={"type": "date"}),
            "ultima_vacuna": forms.DateInput(attrs={"type": "date"})
        }
        # Lanzamos mensaje de error en caso de que no se escriban campos obligarios o no se pongan la cantidad de caracteres correspondientes.
        error_messages = {
            "nombre": {
                "required": "El nombre es obligatorio",
                "max_length": "El nombre de la mascota no puede tener más de 20 caracteres"
            },
            "raza": {
                "required": "La raza es obligatoria",
                "max_length": "La raza no puede tener más de 15 caracteres"
            },
            "peso": {
                "required": "El peso es obligatorio"
            },
            "vacunado": {
                "required": "El campo vacunado es obligatorio"
            },
            "domicilio_duenyo": {
                "max_length": "El domicilio no puede superar 100 caracteres"
            }
        }
