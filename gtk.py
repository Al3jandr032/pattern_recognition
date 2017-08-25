#!/usr/bin/env python
# -*- coding: utf-8 -*-import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, GObject


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        self.set_border_width(10)
        self.set_default_size(400, 200)

        grid = Gtk.Grid()
        self.add(grid)

        self.num_class_label = Gtk.Label("Numero de clases")
        self.num_class = Gtk.Entry()
        self.num_class.set_text("Hello World")
        self.run_button = Gtk.Button(label="Comparar")
        self.run_button.connect("clicked", self.on_button_clicked)
      

        grid.add(self.num_class_label)
        grid.add(self.num_class)
        grid.add(self.run_button)

        """
        grid.attach_next_to(button3, button1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(button4, button3, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach(button5, 1, 2, 1, 1)
        grid.attach_next_to(button6, button5, Gtk.PositionType.RIGHT, 1, 1)

        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)
        """

    def on_button_clicked(self, widget):
        print("Hello World")
        print self.num_class.get_text()

widget = Gtk.Box()
#print(dir(widget.props))

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()