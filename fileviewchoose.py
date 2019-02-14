from kivy.uix.filechooser import FileChooserController, FileChooserLayout 
from kivy.uix.widget import Widget


class ImagePreviewEntry(Widget):
    def is_png(self, filename):
        print 'checking if png', filename
        return (len(filename)>4) and filename[-4:] == '.png'

    def get_image(self, context):
        print context
        if (not context.isdir) and self.is_png(context.name):
            return context.path
        return 'atlas://data/images/defaulttheme/filechooser_%s' % ('folder' if context.isdir else 'file')

class FileChooserImageView(FileChooserController):
    '''Implementation of a :class:`FileChooserController` using an image preview.
    '''
    _ENTRY_TEMPLATE = 'FileImageEntry'

class FileChooserImageLayout(FileChooserLayout):
    '''File chooser layout using an image preview.
    '''

    VIEWNAME = 'images'
    _ENTRY_TEMPLATE = 'FileImageEntry'

    def __init__(self, **kwargs):
        super(FileChooserImageLayout, self).__init__(**kwargs)
        self.fbind('on_entries_cleared', self.scroll_to_top)

    def scroll_to_top(self, *args):
        self.ids.scrollview.scroll_y = 1.0



