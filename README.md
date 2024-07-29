# Maxikioso

## Descripción
Maxikioso es un sistema de gestión de productos que permite agregar, ver y editar productos, así como categorizarlos. También incluye la funcionalidad para buscar productos en la base de datos.

## Funcionalidades
- Agregar productos
- Ver lista de productos
- Editar productos
- Categorizar productos
- Buscar productos

## Instalación
1. Clona el repositorio.
2. Instala las dependencias con `pip install -r requirements.txt`.
3. Realiza las migraciones con `python manage.py makemigrations` y `python manage.py migrate`.
4. Crea un superusuario con `python manage.py createsuperuser`.
5. Ejecuta el servidor de desarrollo con `python manage.py runserver`.

## Uso
- Navega a `http://localhost:8000/` para ver la lista de productos.
- Usa el menú de navegación para agregar, editar productos o buscar productos.
- Para agregar una categoría, navega a `http://localhost:8000/categoria/agregar/`.
- Para buscar productos, navega a `http://localhost:8000/buscar/`.
