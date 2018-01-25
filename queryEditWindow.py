#!/usr/bin/env python

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
        self.projectDir = ''
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        self.execute_query_selection_prefix = 'from dogtail.tree import *; from dogtail.utils import *; app = root.application('org.gnome.Polari');' # make it generic
        self.execute_query_selection_postfix = '[0].blink()'

        self.query_text_view = Gtk.TextView()
        self.query_text_buffer = self.query_text_view.get_buffer()
        self.query_text_view.show()

        query_scroll_window = Gtk.ScrolledWindow()
        query_scroll_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        query_scroll_window.add(self.query_text_view)
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

        steps_text_view = Gtk.TextView()
        self.steps_text_buffer = steps_text_view.get_buffer()
        steps_text_view.show()

        steps_scroll_window = Gtk.ScrolledWindow()
        steps_scroll_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        steps_scroll_window.add(steps_text_view)
        steps_scroll_window.show()

        steps_cancel_button = Gtk.Button('Clear query')
        steps_cancel_button.connect('clicked', self.clear_steps_text_buffer)
        steps_cancel_button.show()

        steps_write_button = Gtk.Button('Write Behave Steps')
        steps_write_button.connect('clicked', self.write_behave_steps)
        steps_write_button.show()

        steps_h_button_box = Gtk.HButtonBox()
        steps_h_button_box.pack_start(steps_write_button, True, True, 0)
        steps_h_button_box.pack_start(steps_cancel_button, True, True, 0)
        steps_h_button_box.show()

        vbox = Gtk.VBox(False, 0)
        vbox.add(query_scroll_window)
        vbox.pack_start(query_h_button_box, False, False, 0)
        vbox.add(steps_scroll_window)
        vbox.pack_start(steps_h_button_box, False, False, 0)
        vbox.show()

        self.window = Gtk.Window()
        self.window.set_resizable(True)
        self.window.connect('destroy', self.close_edit_window)
        self.window.set_title('Dogtail Query - Behave Steps Edit Window')
        self.window.set_border_width(0)
        self.window.add(vbox)
        self.window.show()


    def clear_query_text_buffer(self, widget):
        self.query_text_buffer.set_text('', 0)


    def clear_steps_text_buffer(self, widget):
        self.steps_text_buffer.set_text('', 0)


    def close_edit_window(self, widget):
        self.window.destroy()

    def execute_query_selection(self, widget):
        from subprocess import Popen
        Popen(['python', '-c', self.execute_query_selection_prefix + self.query_text_view.get_text() + self.execute_query_selection_postfix])


    def fill_query_text_buffer(self, widget, app_name, content):
        self.app_name = app_name
        self.query_text_buffer.set_text(content, len(content))


    def fill_steps_text_buffer(self, widget, app_name, content):
        self.app_name = app_name
        self.steps_text_buffer.set_text(content, len(content))

    def set_project_dir(self):
        import os
        from os.path import expanduser, join, exists
        
        if not os.path.exists(join(expanduser('~'), '.config', 'sniff2', 'preferences.csv')):
            os.makedirs(join(expanduser('~'), '.config', 'sniff2')) 
            open(join(expanduser('~'), '.config', 'sniff2', 'preferences.csv'), 'a').close()

        if os.stat(join(expanduser('~'), '.config', 'sniff2', 'preferences.csv')).st_size != 0:
            configFile = open(join(expanduser('~'), '.config', 'sniff2', 'preferences.csv'), 'r')
            self.projectDir = configFile.readline()
        else:
            self.projectDir = join(expanduser('~'), 'dogtail-behave-projects', self.app_name)


    def write_dogtail_query(self, widget):
        print('=== writing dogtail query ===')
        import os
        from os.path import join, exists
        
        self.set_project_dir()
        if not exists(join(self.projectDir, 'features', 'steps')):
            os.makedirs(join(self.projectDir, 'features', 'steps'))

        query = open(join(self.projectDir, 'features', 'steps', 'steps.py'), 'wb') #dont forget to change it to 'ab' mode
        query.write(self.query_text_buffer.get_text(self.query_text_buffer.get_start_iter(), self.query_text_buffer.get_end_iter(), include_hidden_chars = True))
        query.close()
        print('=== done writing dogtail query ===\n')


    def write_behave_steps(self, widget):
        print('=== writing behave steps ===')
        import os
        from os.path import join, exists
        
        self.set_project_dir()
        if not exists(join(self.projectDir, 'features')):
            os.makedirs(join(self.projectDir, 'features'))

        steps = open(join(self.projectDir, 'features', 'general.feature'), 'wb') #dont forget to change it to 'ab' mode
        steps.write(self.steps_text_buffer.get_text(self.steps_text_buffer.get_start_iter(), self.steps_text_buffer.get_end_iter(), include_hidden_chars = True))
        steps.close()
        print('=== done writing behave steps ===\n')


def main():
    Gtk.main()
    return 0

if __name__ == '__main__':
    QueryEditWindow()
    main()

