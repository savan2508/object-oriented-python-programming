import time
import webbrowser

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard

from filesharer import FileSharer

Builder.load_file('frontend.kv')


class CameraScreen(Screen):

    def start(self):
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        current_time = time.strftime('%Y%m%d-%H%H%S')
        self.file_name = f"files/{current_time}.png"
        self.ids.camera.export_to_png(self.file_name)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.file_name


class ImageScreen(Screen):

    def create_link(self):
        file_path = App.get_running_app().root.ids.camera_screen.file_name
        fileshare = FileSharer(filepath=file_path)
        self.url = fileshare.share()
        self.ids.link.text = self.url

    def copy_link(self):
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = "Create a link first"

    def open_link(self):
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = "Please create a link first"


class RootWidget(ScreenManager):
    pass


class RunApp(App):

    def build(self):
        return RootWidget()


RunApp().run()
