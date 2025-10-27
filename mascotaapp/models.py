from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date

class Mascota(models.Model):
    nombre = models.CharField(max_length=20)
    raza = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    
# Peso con validadores para asegurar rango entre 0.01 y 200 kg
    peso = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[
            MinValueValidator(0.01, message="El peso debe estar entre 10 gramos y 200 kilos"),
            MaxValueValidator(200, message="El peso debe estar entre 10 gramos y 200 kilos")
        ]
    )

    vacunado = models.BooleanField(default=False)
    ultima_vacuna = models.DateField(null=True, blank=True)  
    email_duenyo = models.EmailField(null=True, blank=True)
    domicilio_duenyo = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombre

    def clean(self):
        
        # Validaciones condicionales:
        # - ultima_vacuna obligatoria si vacunado es True
        # - ultima_vacuna posterior a fecha_nacimiento
        
        super().clean()
        errores = {}

        if self.vacunado:
            if not self.ultima_vacuna:
                errores['ultima_vacuna'] = "Por favor, introduce la fecha de la última vacuna"
            elif self.ultima_vacuna <= self.fecha_nacimiento:
                errores['ultima_vacuna'] = "La fecha de la última vacunación debe ser posterior a la fecha de nacimiento"

        if errores:
            raise ValidationError(errores)
