# Mascotaproyecto

Proyecto de simulacro de defensa sobre Python y Django: registro de mascotas con formulario y validaciones.

## Descripción

Este proyecto consiste en una aplicación Django llamada **mascotaapp** que permite registrar mascotas a través de un formulario web.  
Se practican conceptos clave de Django: modelos, formularios, vistas, URLs, plantillas y validaciones.

## Estructura

- **Proyecto:** `mascotaproyecto`  
- **Aplicación:** `mascotaapp`  
- **Modelo principal:** `Mascota`  
- **Formulario:** `MascotaForm`  
- **Vista:** `miform`  
- **Ruta:** `/mascotaapp/miform/`  

## Funcionalidad

El formulario permite registrar las siguientes propiedades de la mascota:

- **nombre**: cadena de texto, obligatorio, máximo 20 caracteres  
- **raza**: cadena de texto, obligatorio, máximo 15 caracteres  
- **fecha_nacimiento**: fecha, obligatorio  
- **peso**: número decimal, obligatorio, entre 0,01 y 200 kilos  
- **vacunado**: booleano, obligatorio  
- **ultima_vacuna**: fecha, obligatorio solo si la mascota está vacunada, debe ser posterior a fecha_nacimiento  
- **email_duenyo**: email, opcional  
- **domicilio_duenyo**: texto, opcional, máximo 100 caracteres  

### Validaciones

- Validaciones simples (requerido, longitud, rango) se gestionan en el **ModelForm**.  
- Validaciones condicionales (fecha de última vacuna) se gestionan en el **modelo (`clean()`)**, asegurando consistencia incluso fuera del formulario.  
- Los campos de fecha usan **widgets de calendario** para facilitar la introducción de datos.

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/TU_USUARIO/mascotaproyecto.git
cd mascotaproyecto
