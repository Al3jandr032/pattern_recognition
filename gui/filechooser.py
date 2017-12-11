import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os
import numpy as np
from scipy.io import wavfile as w
from scikits.talkbox.features import mfcc


def create_ceps(fn):
  print "creating :",fn
  sample_rate, X = w.read(fn)
  ceps, mspec, spec = mfcc(X)
  num_ceps = len(ceps)
  return [np.mean(ceps[int(num_ceps*1/10):int(num_ceps*9/10)], axis=0)]

class FileChooserWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Music classifier")
        self.set_border_width(10)
        self.set_default_size(400, 200)
        self.filename = None

        box = Gtk.Box(spacing=6)
        self.add(box)

        button1 = Gtk.Button("Choose File")
        button1.connect("clicked", self.on_file_clicked)
        box.add(button1)

        label1 = Gtk.Label()
        label1.set_text("Select on wav file to classify.\nThen press the button")
        label1.set_justify(Gtk.Justification.LEFT)
        box.add(label1)

        button_process = Gtk.Button("Process")
        button_process.connect("clicked", self.on_proces_clicked)
        box.add(button_process)
       
    def on_proces_clicked(self,widget):
        print "on_proces_clicked"
        ceps = create_ceps(self.filename)
        print ceps
        arraylist = []
        for i in ceps:
            for elem in i:
                arraylist.append([elem])
        print arraylist

    def on_file_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
            self.filename = dialog.get_filename()
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

    

win = FileChooserWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()