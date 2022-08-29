from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.pickers import MDTimePicker
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.screenmanager import ScreenManager, Screen


class Hello(MDApp):
    dialog = None

    def build(self):
        self.theme_cls.material_style = "M3"
        return Builder.load_file("Main.kv")

    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.open()

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Oops! Sizning telingiz kompga bog'lanib qoldi uzr!",
                radius=[20, 7, 20, 7],
            )
        self.dialog.open()

    def video_state(self):
        state = 'play'
        return state

    def video_playback(self):
        player = VideoPlayer(source="hello.mp4")
        player.state = 'play'
        player.options = {'eos': 'loop'}
        player.allow_stretch = True
        return player


# Add_videos
class MenuScreen(Screen):
    pass


class UploadScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class AddVideo(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='screen 1'))
sm.add_widget(AddVideo(name='video'))

if __name__ == "__main__":
    Hello().run()
