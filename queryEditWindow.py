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
        query_text_view = Gtk.TextView()
        self.query_text_buffer = query_text_view.get_buffer()
        query_text_view.show()

        query_scroll_window = Gtk.ScrolledWindow()
        query_scroll_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        query_scroll_window.add(query_text_view)
        query_scroll_window.show()

        query_cancel_button = Gtk.Button('Clear query')
        query_cancel_button.connect('clicked', self.clear_query_text_buffer)
        query_cancel_button.show()

        query_write_button = Gtk.Button('Write Dogtail Query')
        query_write_button.connect('clicked', self.write_dogtail_query)
        query_write_button.show()

        query_h_button_box = Gtk.HButtonBox()
        query_h_button_box.pack_start(query_write_button, True, True, 0)
        query_h_button_box.pack_start(query_cancel_button, True, True, 0)
        query_h_button_box.show()

        vbox = Gtk.VBox(False, 0)
        vbox.add(query_scroll_window)
        vbox.show()
        vbox.pack_start(query_h_button_box, False, False, 0)

        window = Gtk.Window()
        window.set_resizable(True)
        window.connect('destroy', self.close_edit_window)
        window.set_title('Dogtail Query - Behave Steps Edit Window')
        window.set_border_width(0)
        window.add(vbox)
        window.show()


    def clear_query_text_buffer(self, widget):
        self.query_text_buffer.set_text('', 0)


    def close_edit_window(self, widget):
        Gtk.main_quit()


    def fill_query_text_buffer(self, widget, app_name, content):
        self.app_name = app_name
        self.query_text_buffer.set_text(content, len(content))


    def write_dogtail_query(self, widget):
        print('=== writing dogtail query ===')
        import os
        from os.path import expanduser, join, exists
        projectDir = join(expanduser('~'), 'dogtail-behave-projects', self.app_name)
        if not exists(join(projectDir, 'features', 'steps')):
            os.makedirs(join(projectDir, 'features', 'steps'))

        query = open(join(projectDir, 'features', 'steps', 'steps.py'), 'wb') #dont forget to change it to 'ab' mode
        query.write(self.query_text_buffer.get_text(self.query_text_buffer.get_start_iter(), self.query_text_buffer.get_end_iter(), include_hidden_chars = True))
        query.close()
        print('=== done writing dogtail query ===\n')


def main():
    Gtk.main()
    return 0

if __name__ == '__main__':
    QueryEditWindow()
    main()

