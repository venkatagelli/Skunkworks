# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 21:01:35 2020

@author: VENKATA
"""

#computer vision - env 
import pyvista as pv 
from pyvista import examples

filename = 'E:/planeRCNN/output/planes.ply'

print(filename)

mesh = pv.read(filename)
cpos = mesh.plot()

plotter = pv.Plotter(off_screen= True)
plotter.add_mesh(mesh)
plotter.show(screenshot="myscreenshot.png")