# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 19:45:26 2020

@author: UGAC003
"""

import sys
sys.path.append('../')

import vis as gra

import vtk

# an array to store cubes
cube_list = []

# room dims

X = 50
Y = 50
Z = 50


# the actor
actor = vtk.vtkActor()
# the renderer 
render = vtk.vtkRenderer()

# loop to draw 10 cubes in 2 parallel lines
for i in range(X):
    for k in range(Z):
        actor = gra.cube_from_source(i, 0, k, 1, 'extWallInert', 0)
        # adding the actor
        render.AddActor(actor)
        actor = gra.cube_from_source(i, Y - 1, k, 1, 'extWallInert', 0)
        # adding the actor   
        render.AddActor(actor)
    
# loop to draw 10 cubes in 2 parallel lines perpedicular to the above
for j in range(Y):
    for k in range(Z):
        actor = gra.cube_from_source(0, j, k, 1, 'extWallInert', 0)
        # adding the actor
        render.AddActor(actor)
        actor = gra.cube_from_source(X - 1, j, k, 1, 'extWallInert', 0)
        # adding the actor   
        render.AddActor(actor)
    
# for k in range(Z):
#     actor = cube_from_source(0,0,k)
#     # adding the actor
#     render.AddActor(actor)
#     actor = cube_from_source(0, X, k)
#     # adding the actor   
#     render.AddActor(actor)

#the rendering window and adding the renderer
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(render)

#the interactor so we can interact with the cube or anything is drawn
renWinIn = vtk.vtkRenderWindowInteractor()
renWinIn.SetRenderWindow(renWin)

#load the window
renWinIn.Start()

#iterate and print vertices from the list of cubes
for cube in cube_list:
    #print(cube)
    cubePolyData = cube.GetOutput()
    #print(cubePolyData)
    vertices = cubePolyData.GetPoints().GetData()
    #print(vertices)

 