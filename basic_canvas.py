import os
os.environ['KIVY_BCM_DISPMANX_ID'] = '4'

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle, Line

from kivy.properties import ObjectProperty

from kivy.lang import Builder

from fileviewchoose import FileChooserImageView, ImagePreviewEntry

Builder.load_file('app.kv')

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class ExitScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

class DrawingScreen(Screen):
    pass

class PicturesScreen(Screen):
    pass

class MNISTCanvas(Widget):
    """
    Our application main widget, derived from touchtracer example, use data
    constructed from touches to match symboles loaded from my_gestures.

    """
    def __init__(self, *args, **kwargs):
        super(MNISTCanvas, self).__init__(*args, **kwargs)
        self.desired_size = (280,280)
        self.size = self.desired_size 
        with self.canvas:
            Color(1,1,1)
            Rectangle(pos=(333,100), size=self.size)


    def on_touch_down(self, touch):
        # start collecting points in touch.ud
        # create a line to display the points
        userdata = touch.ud
        if self.collide_point(touch.x, touch.y):
            with self.canvas:
                Color(0, 0, 0)
                d = 30.
                userdata['line'] = Line(points=(touch.x, touch.y), width=5)
            return True
        else:
            return False

    def on_touch_move(self, touch):
        # store points of the touch movement
        try:
            if self.collide_point(touch.x, touch.y):
                touch.ud['line'].points += [touch.x, touch.y]
                return True
            else:
                return False
        except (KeyError) as e:
            pass

    def on_touch_up(self, touch):
        pass
       
    def save_canvas(self):
        self.export_to_png('drawing.png')

    def clear(self):
        self.canvas.clear()
        self.size = self.desired_size 
        with self.canvas:
            Color(1,1,1)
            Rectangle(pos=self.pos, size=self.size)
            print self.size, self.pos

class DemoGesture(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(DrawingScreen(name='canvas'))
        sm.add_widget(ExitScreen(name='quitter'))
        sm.add_widget(PicturesScreen(name='pics'))
        self.sm = sm
        self.mnist = self.sm.get_screen('canvas').ids.mnist
        return self.sm
    
    def clear(self):
        self.mnist.clear()

    def save_and_quit(self):
        print 'Saving'
        self.mnist.save_canvas()
        self.stop()

    def on_stop(self, save=False):
        print 'Quitting'
        super(DemoGesture, self).on_stop()
 

if __name__ == '__main__':
    DemoGesture().run()
