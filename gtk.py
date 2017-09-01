#!/usr/bin/env python
# -*- coding: utf-8 -*-import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, GObject
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from generator import ClassGenerator
from generator import ClassHolder
from Clasifier import EculedianDistance
from Clasifier import Mahalanobis
from Clasifier import MaxProbability

classifiers = [EculedianDistance(),Mahalanobis(),MaxProbability()]

class MyWindow(Gtk.Window):

    
    def __init__(self):
        Gtk.Window.__init__(self, title="capp")
        self.set_border_width(10)
        self.set_default_size(400, 200)

        self.Classifier = {'index':-1,'name':None}
        self.filePath = None
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.colors = ['b', 'g', 'c', 'm', 'y','k']
        self._x = 0
        self._y = 0

        header = Gtk.HeaderBar(title="Pattern Recognition")
        header.set_subtitle("Classifier")
        header.props.show_close_button = True

        self.set_titlebar(header)

        box = Gtk.Box(spacing=6)
        self.add(box)

        button1 = Gtk.Button("Choose File")
        button1.connect("clicked", self.on_file_clicked)
        box.add(button1)

        name_store = Gtk.ListStore(int, str)
        name_store.append([0, "Eculedian"])
        name_store.append([1, "Mahalanobis"])
        name_store.append([2, "MaxProbability"])
    

        name_combo = Gtk.ComboBox.new_with_model_and_entry(name_store)
        name_combo.connect("changed", self.on_name_combo_changed)
        name_combo.set_entry_text_column(1)

        box.add(name_combo)
        
        self._xEntry = Gtk.Entry()
        box.add(Gtk.Label("Coordenada x"))
        box.add(self._xEntry)

        self._yEntry = Gtk.Entry()
        box.add(Gtk.Label("Coordenada y"))
        box.add(self._yEntry)

        self._lEntry = Gtk.Entry()
        self._lEntry.set_text("20")
        box.add(Gtk.Label("Limite"))
        box.add(self._lEntry)

        run_button = Gtk.Button(label="Classify")
        run_button.connect("clicked", self.on_button_clicked)
        box.add(run_button)

        plot_button = Gtk.Button(label="Close plot")
        plot_button.connect("clicked", self.on_button_plot)
        box.add(plot_button)
        self.f = Figure(figsize=(5, 4), dpi=100)
        canvas = FigureCanvas(self.f)  # a Gtk.DrawingArea
        canvas.set_size_request(800, 600)
        #sw.add_with_viewport(canvas)
        box.add(canvas)

    def on_name_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            row_id, name = model[tree_iter][:2]
            print("Selected: ID=%d, name=%s" % (row_id, name))
            self.Classifier['index']=row_id
            self.Classifier['name']= name
        else:
            entry = combo.get_child()
            print("Entered: %s" % entry.get_text())

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
            self.filePath = dialog.get_filename()
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def on_button_plot(self,widget):
        plt.close('all')

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
        print self.Classifier['index']
        print self.Classifier['name']
        x=0
        y=0
        l=0
        if len(self._xEntry.get_text()) > 0:
            x = int(self._xEntry.get_text())
        if len(self._yEntry.get_text()) > 0:
            y = int(self._yEntry.get_text())
        if len(self._lEntry.get_text()) > 0:
            l = int(self._lEntry.get_text())

        a = ClassGenerator(size=100,config_path=self.filePath)
        holder = ClassHolder(a.generate(),plotfig=self.f)
        plot = holder.classify(classifiers[self.Classifier['index']],x,y,l) 
        if plot != None:
            #print plot
            plot.show()


widget = Gtk.Box()
#print(dir(widget.props))

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()