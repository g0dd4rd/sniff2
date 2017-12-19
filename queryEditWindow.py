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
        text_view = Gtk.TextView()
        text_buffer = text_view.get_buffer()
        text_view.show()

        scroll_window = Gtk.ScrolledWindow()
        scroll_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scroll_window.add(text_view)
        scroll_window.show()

        write_button = Gtk.Button('Write query')
        write_button.connect('clicked', self.write_query)
        #write_button.set_flags(Gtk.CAN_DEFAULT)
        write_button.show()

        h_button_box = Gtk.HButtonBox()
        h_button_box.pack_start(write_button, True, True, 0)
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


    def close_query_edit_window(self, widget):
        Gtk.main_quit()


    def write_query(self, widget):
        print('writing dogtail query')


def main():
    Gtk.main()
    return 0

if __name__ == '__main__':
    QueryEditWindow()
    main()

