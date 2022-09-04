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


class MyGridLayout(Widget):

    url = ObjectProperty(None)
    name = ObjectProperty(None)
    exito_label = ObjectProperty(None)

    def download_courses(self):
        self.ids.exito_label.text = 'Espera tu video esta descargando...'
        a = open(os.devnull, 'w')
        url = self.ids.url.text
        print(url)
        nombre = self.ids.name.text
        print(nombre)
        ruta = nombre+'.mp4'
        # self.url.text = ''
        # self.name.text = ''
        # self.add_widget(Label(text='Procesando... ', font_size=30))
        print('procesando...')
        # url = "https://dffm5yppba5na.cloudfront.net/output/hls/coursesclassesvideos2puenteelcantordefonsecaconbajos.m3u8"
        command = ['ffmpeg', '-protocol_whitelist',
                   'file,http,https,tcp,tls,crypto',
                   '-i', url, '-c', 'copy', ruta]
        p = subprocess.call(command, stdout=a, stderr=subprocess.STDOUT)

        if p == 0:
            self.ids.exito_label.text = 'Descarga exitosa'
            os.startfile(
                "C:/Users/luisf/Desktop/code/pyscripts/video_downloader")
        else:
            self.ids.exito_label.text = 'Descarga exitosa'
        return p


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
