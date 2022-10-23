import pdb
import subprocess
import os
import sys
from pydrive.google_drive import subir_archivo
from colorama import Fore

def download_m3u8(url, nombre_archivo, ruta):
    print(Fore.CYAN +'[*] Listo, tu video esta descargando...')
    a = open(os.devnull, 'w')
    # url = self.ids.url.text
    # url = 'https://dffm5yppba5na.cloudfront.net/output/hls/coursesclassesvideos2puenteelcantordefonsecaconbajos.m3u8'

    # print(url)
    ruta = ruta.split('/')
    cd = []

    newpath = os.getcwd()
    if len(ruta) > 0:
        # print(ruta)
        folder = '/'.join(ruta)
        newpath = os.path.join(os.getcwd(), folder)
        # print(newpath)
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        cd = ['cd', folder, '&&']
        # print(folder)
    print(Fore.BLACK + '[*] PROCESANDO...')
    # url = "https://dffm5yppba5na.cloudfront.net/output/hls/coursesclassesvideos2puenteelcantordefonsecaconbajos.m3u8"
    command = cd + ['ffmpeg', '-protocol_whitelist',
                'file,http,https,tcp,tls,crypto',
                '-i', url, '-c', 'copy', nombre_archivo +'.mp4']
    # p = subprocess.call(command, stdout=a, stderr=subprocess.STDOUT)
    try:
        # todo: desactivar el retorno de la ejecución
        subprocess.run(command, check=True, shell=True)
        print(Fore.CYAN + "[*] Video descargado con exito :')")
        directory = newpath or os.getcwd()
        subir_archivo(nombre_archivo, f'{directory}\\{nombre_archivo}.mp4')
        os.startfile(newpath or os.getcwd())

    except subprocess.CalledProcessError as e:
        raise ValueError(f'Ocurrio un error al realizar la descarga :( \n {e}')
