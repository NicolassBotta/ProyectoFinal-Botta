# Proyecto Django con Patrón MVT

## Funcionalidades

1. **Herencia de HTML:** Todas las plantillas extienden de `padre.html`.
2. **Modelos:** Tres clases definidas en `models.py` (`Curso`, `Estudiante`, `Profesor`).
3. **Formularios para insertar datos:** Formularios disponibles en:
   - `app-coder/cursoformulario/`
   - `app-coder/estudianteformulario/`
   - `app-coder/profesorformulario/`
4. **Formulario para buscar en la BD:** Formulario disponible en `app-coder/busquedacamada/`.

## Cómo Probar

1. Ejecutar el servidor de desarrollo:
    python manage.py runserver
2. Abrir un navegador web y visitar:
    - Para agregar cursos: `http://127.0.0.1:8000/app-coder/curso-formulario/`
    - Para agregar estudiantes: `http://127.0.0.1:8000/app-coder/estudianteformulario/`
    - Para agregar profesores: `http://127.0.0.1:8000/app-coder/profesorformulario/`
    - Para buscar cursos: `http://127.0.0.1:8000/app-coder/busquedacamada/`

