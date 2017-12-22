#!/usr/bin/env python

#import pygtk
#pygtk.require('2.0')
#import gtk
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
import sys
import pyatspi
import Accessibility
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import Gio
from gi.repository import GdkPixbuf
from gi.repository import GObject
from gi.repository import GLib

class QueryEditWindow:
    def __init__(self):
        self.app_name = 'example-app'
        text_view = Gtk.TextView()
        self.text_buffer = text_view.get_buffer()
        text_view.show()

        scroll_window = Gtk.ScrolledWindow()
        scroll_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scroll_window.add(text_view)
        scroll_window.show()

        cancel_button = Gtk.Button('Clear query')
        cancel_button.connect('clicked', self.clear_text_buffer)
        cancel_button.show()

        write_button = Gtk.Button('Write Behave Steps')
        write_button.connect('clicked', self.write_behave_steps)
        #write_button.set_flags(Gtk.CAN_DEFAULT)
        write_button.show()

        h_button_box = Gtk.HButtonBox()
        h_button_box.pack_start(write_button, True, True, 0)
        h_button_box.pack_start(cancel_button, True, True, 0)
        h_button_box.show()

        scroll_vbox = Gtk.VBox(False, 0)
        scroll_vbox.add(scroll_window)
        scroll_vbox.show()
        scroll_vbox.pack_start(h_button_box, False, False, 0)

        window = Gtk.Window()
        window.set_resizable(True)
        window.connect('destroy', self.close_query_edit_window)
        window.set_title('Dogtail Query Edit Window')
        window.set_border_width(0)
        window.add(scroll_vbox)
        window.show()


    def clear_text_buffer(self, widget):
        self.text_buffer.set_text('', 0)


    def close_query_edit_window(self, widget):
        Gtk.main_quit()


    def fill_text_buffer(self, widget, app_name, content):
        self.app_name = app_name
        self.text_buffer.set_text(content, len(content))


    def write_behave_steps(self, widget):
        print('=== writing behave steps ===')
        import os
        from os.path import expanduser, join, exists
        projectDir = join(expanduser('~'), 'dogtail-behave-projects', self.app_name)
        if not exists(join(projectDir, 'features', 'steps')):
            os.makedirs(join(projectDir, 'features', 'steps'))

        steps = open(join(projectDir, 'features', 'steps', 'steps.py'), 'wb') #dont forget to change it to 'ab' mode
        steps.write(self.text_buffer.get_text(self.text_buffer.get_start_iter(), self.text_buffer.get_end_iter(), include_hidden_chars = True))
        steps.close()


def main():
    Gtk.main()
    return 0

if __name__ == '__main__':
    QueryEditWindow()
    main()

