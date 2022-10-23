from ffmpeg_handler.core import download_m3u8

def cli():
    print('Ingrese una url (.m3u8) para descargar contenido...\n')
    url = input('Url: ')
    nombre_archivo= input('Nombre del archivo: ')
    ruta  = input('Ruta (opcional): ') or 'videos_m3u8'
    download_m3u8(url, nombre_archivo, ruta)