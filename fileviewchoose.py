from kivy.uix.filechooser import FileChooserController, FileChooserLayout 
from kivy.uix.widget import Widget

from os.path import (
    basename, join, sep, normpath, expanduser, altsep,
    splitdrive, realpath, getsize, isdir, abspath, isfile, dirname)
from weakref import ref


class ImagePreviewEntry(Widget):
    def is_png(self, filename):
        return (len(filename)>4) and filename[-4:] == '.png'

    def get_image(self, context):
        if (not context.isdir) and self.is_png(context.name):
            return context.path
        return 'atlas://data/images/defaulttheme/filechooser_%s' % ('folder' if context.isdir else 'file')

class FileChooserImageView(FileChooserController):
    '''Implementation of a :class:`FileChooserController` using an image preview.
    '''
    _ENTRY_TEMPLATE = 'FileImageEntry'

    def _generate_file_entries(self, *args, **kwargs):
        # generate all the entries in the main directory
        path = kwargs.get('path', self.path)
        try:
            for index, total, item in self._add_files(path):
                yield index, total, item
        except OSError:
            Logger.exception('Unable to open directory <%s>' % self.path)
            self.files[:] = []


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



