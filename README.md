# Video Streamer

Herramienta Linux para reproducir URLs de video en HDMI a pantalla completa, con control web remoto.

## Instalación

1. Instala las dependencias necesarias:

   ```bash
   sudo apt-get install mpv jq ffmpeg python3-flask
   ```

2. (Opcional) crea un entorno virtual y activa:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r web-admin/requirements.txt
   ```

## Uso

Para iniciar la interfaz web ejecuta:

```bash
python3 web-admin/app.py
```

Las credenciales por defecto son `admin`/`streamer`. Puedes cambiarlas mediante variables de entorno:

```bash
export STREAM_USER="usuario"
export STREAM_PASSWORD="contraseña"
```

La ruta del archivo de configuración y del script de streaming también pueden personalizarse con `STREAM_CONFIG_PATH` y `STREAM_SCRIPT_PATH`.

## Requisitos
- `mpv`
- `jq`
- `ffmpeg`
- `flask`
