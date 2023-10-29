# Magslator WEB-APP

## Descripción

Este proyecto representa la versión web de una aplicación diseñada para la traducción automática de mangas del japonés al español. Esta iniciativa se desarrolla como parte del curso "CC6409: Taller de Desarrollo de Proyectos de IA".

## Instalación

1. Clonar repositorio:

```bash
git clone [insert repository URL]
```

2. Crear un virtualenv (versión originar de python 3.11), por ejemplo:

```bash
python3 -m venv venv
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Correr aplicación:

```bash
python app/app.py
```

## Uso

Por supuesto, aquí está la versión corregida de tu lista:

1. Accede a la página web a través de `localhost:5000`. Al ejecutar la aplicación, se debería crear automáticamente una carpeta llamada `uploads_files` **FUERA** del directorio raíz. Si no se crea, hazlo manualmente.
2. Utiliza el botón `Examinar...` para subir imágenes a la página.
3. Después de subir las imágenes, presiona el botón `Subir imágenes`. De lo contrario, las imágenes se perderán.
4. Una vez subidas las imágenes, utiliza el botón `Galerías`. Esto cambiará la ruta a `/gallery`.
5. En la galería, puedes ver las imágenes que has subido. Es posible navegar entre todas las imágenes subidas que se encuentran en la carpeta `uploads_files` utilizando los botones `Anterior` y `Siguiente`.
