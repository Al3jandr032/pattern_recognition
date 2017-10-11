#!/usr/bin/env python
# -*- coding: utf-8 -*-import sys
import Tkinter
import tkMessageBox
from PIL import Image, ImageTk
import sys
import numpy as np
from classholder import ClassHolder
from Clasifier import MaxProbability
from Clasifier import EuclideanDistance
from Clasifier import Mahalanobis
from Clasifier import KNN

points = []
#sudo apt-get install python-imaging-tk
def callback(event):
		#print "clicked at: ", event.x, event.y
		points.append({'x':event.x,'y':event.y})
		if(len(points)%10 == 0 and len(points) < 30):
			tkMessageBox.showinfo("Mensaje", "Has seleccionado : "+str(len(points))+"muestras")
		if(len(points) == 30):
			tkMessageBox.showinfo("Mensaje", "Has seleccionado : "+str(len(points))+" muestras, ahora selecciona la muestra a clasificar")
		elif(len(points) > 30):
			globals()['window'].destroy()

window = Tkinter.Tk(className="Image")
classList = ClassHolder()


if __name__ == "__main__":
	if len(sys.argv) > 1:
		
		im = Image.open(sys.argv[1])
		canvas = Tkinter.Canvas(window, width=im.size[0], height=im.size[1])
		canvas.pack()
		image_tk = ImageTk.PhotoImage(im)
		canvas.create_image(im.size[0]//2, im.size[1]//2, image=image_tk)
		canvas.bind("<Button-1>", callback)
		Tkinter.mainloop()
		image = Image.open(sys.argv[1])
		pix = image.load()
		 #Get the RGBA Value of the a pixel of an image
		if(len(points) == 31):
			for c in range(0,3):
				holder = [[],[],[]]
				for i in range(0+(10*c),10+(10*c)):
					rgb = pix[points[i]['x'],points[i]['y']]
					holder[0].append(rgb[0])
					holder[1].append(rgb[1])
					holder[2].append(rgb[2])
				_class = np.array(holder)
				classList.addClass(_class)
				
			for i in range(0,classList.getNumClasses()):
				print classList.average(classList.getClass(i))	
			plist = pix[points[30]['x'],points[30]['y']]
			classList.classify(KNN(),plist[0:3],-1)
	else:
		print "uso : {} <file>".format(sys.argv[0])
