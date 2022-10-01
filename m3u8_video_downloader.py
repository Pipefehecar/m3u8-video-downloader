from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder
import subprocess
import os
from kivy.core.window import Window
Window.size = (800, 600)

Builder.load_file('boxlayouts.kv')
# Builder.load_file('my.kv')

# ffmpeg -protocol_whitelist tcp,tls,https -i "https://dffm5yppba5na.cloudfront.net/output/hls/coursesclassesvideos2puenteelcantordefonsecaconbajos.m3u8" -c copy video.mkv
class MyGridLayout(Widget):

    url = ObjectProperty(None)
    name = ObjectProperty(None)
    exito_label = ObjectProperty(None)

    def download_courses(self):
        self.ids.exito_label.text = 'Espera tu video esta descargando...'
        a = open(os.devnull, 'w')
        # url = self.ids.url.text
        url = 'https://dffm5yppba5na.cloudfront.net/output/hls/coursesclassesvideos2puenteelcantordefonsecaconbajos.m3u8'
        print(url)
        ruta = self.ids.name.text.split('/')
        cd = []
        nombre_archivo = ruta.pop()
        newpath = os.getcwd()
        if len(ruta) > 0:
            print(ruta)
            folder = '/'.join(ruta)
            newpath = os.path.join(os.getcwd(), folder)
            print(newpath)
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            cd = ['cd', folder, '&&']
        print(nombre_archivo)
        ruta = nombre_archivo +'.avi'
        self.ids.url.text = ''
        self.ids.name.text = ''
        self.ids.exito_label.text = 'Procesando... '
        print('procesando...')
        # url = "https://dffm5yppba5na.cloudfront.net/output/hls/coursesclassesvideos2puenteelcantordefonsecaconbajos.m3u8"
        command = cd + ['ffmpeg', '-protocol_whitelist',
                   'file,http,https,tcp,tls,crypto',
                   '-i', url, '-c', 'copy', ruta]
        # p = subprocess.call(command, stdout=a, stderr=subprocess.STDOUT)
        try:
            p = subprocess.run(command, check=True, shell=True)
            self.ids.exito_label.text = 'Descarga exitosa'
            os.startfile(newpath or os.getcwd())

        except subprocess.CalledProcessError as e:
            print(e)
            self.ids.exito_label.text = 'Ocurrio un error al realizar la descarga :('




class DownloaderApp(App):
    def build(self):
        self.title = 'm3u8 video downloader'
        return MyGridLayout()


# class FirstApp(App):

#     def build(self):
#         return Label(text='Hello World')


# download_courses()

if __name__ == '__main__':
    DownloaderApp().run()
