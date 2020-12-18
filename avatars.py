import vtk
import numpy as np


class cube:

    def __init__(self):
        self.source =  vtk.vtkCubeSource()

        self.mapper = vtk.vtkPolyDataMapper()
        self.mapper.SetInputConnection(self.source.GetOutputPort())
        self.mapper.Update()

        self.actor=vtk.vtkActor()
        self.actor.SetMapper(self.mapper)

    def set_dims(self,x,y,z):
        self.source.SetXLength(x)
        self.source.SetYLength(y)
        self.source.SetZLength(z)
        self.source.Update()

    def set_colour(self,r,g,b):
        self.actor.GetProperty().SetColor(r,g,b)

    def get_actor(self):
        return self.actor

    def set_pos(self,x,y,z):
        self.actor.SetPosition(x,y,z)

    def set_ori(self,a,b,c):
        self.actor.SetOrientation(a,b,c)

    def get_pos(self):
        return self.actor.GetPosition()

    def get_bounds(self):
        return self.actor.GetBounds()

    def get_ori(self):
        return self.actor.GetOrientation()

    def plus_x(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0]+dist,cur_pos[1],cur_pos[2])

    def minus_x(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0]-dist,cur_pos[1],cur_pos[2])

    def plus_y(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0],cur_pos[1]+dist,cur_pos[2])

    def minus_y(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0],cur_pos[1]-dist,cur_pos[2])

    def plus_z(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0],cur_pos[1],cur_pos[2]+dist)

    def minus_z(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0],cur_pos[1],cur_pos[2]-dist)


    def turn_red(self):
        self.actor.GetProperty().SetColor(255,0,0)
    def turn_green(self):
        self.actor.GetProperty().SetColor(0,255,0)
    def turn_blue(self):
        self.actor.GetProperty().SetColor(0,0,255)
    def turn_white(self):
        self.actor.GetProperty().SetColor(255,255,255)
    def turn_silver(self):
        self.actor.GetProperty().SetColor(192,192,192)
    def turn_orange(self):
        self.actor.GetProperty().SetColor(1, 0.7, 0.1)



class sphere:

    def __init__(self):
        self.source = vtk.vtkSphereSource()

        self.mapper = vtk.vtkPolyDataMapper()
        self.mapper.SetInputConnection(self.source.GetOutputPort())
        self.mapper.Update()

        self.actor=vtk.vtkActor()
        self.actor.SetMapper(self.mapper)

    def set_center(self,x,y,z):
        self.source.SetCenter(x,y,z)
        self.source.Update()

    def set_dims(self,r,phi_res=100,theta_res=100):
        self.source.SetRadius(r)
        self.source.SetPhiResolution(phi_res)
        self.source.SetThetaResolution(theta_res)        
        self.source.Update()

    def set_colour(self,r,g,b):
        self.actor.GetProperty().SetColor(r,g,b)

    def get_actor(self):
        return self.actor

    def set_pos(self,x,y,z):
        self.actor.SetPosition(x,y,z)

    def set_ori(self,a,b,c):
        self.actor.SetOrientation(a,b,c)

    def get_pos(self):
        return self.actor.GetPosition()

    def get_bounds(self):
        return self.actor.GetBounds()

    def get_ori(self):
        return self.actor.GetOrientation()

    def plus_x(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0]+dist,cur_pos[1],cur_pos[2])

    def minus_x(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0]-dist,cur_pos[1],cur_pos[2])

    def plus_y(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0],cur_pos[1]+dist,cur_pos[2])

    def minus_y(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0],cur_pos[1]-dist,cur_pos[2])

    def plus_z(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0],cur_pos[1],cur_pos[2]+dist)

    def minus_z(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0],cur_pos[1],cur_pos[2]-dist)

    def turn_red(self):
        self.actor.GetProperty().SetColor(255,0,0)
    def turn_green(self):
        self.actor.GetProperty().SetColor(0,255,0)
    def turn_blue(self):
        self.actor.GetProperty().SetColor(0,0,255)
    def turn_white(self):
        self.actor.GetProperty().SetColor(255,255,255)
    def turn_silver(self):
        self.actor.GetProperty().SetColor(192,192,192)


class cone:

    def __init__(self):
        self.source =  vtk.vtkConeSource()

        self.mapper = vtk.vtkPolyDataMapper()
        self.mapper.SetInputConnection(self.source.GetOutputPort())
        self.mapper.Update()

        self.actor=vtk.vtkActor()
        self.actor.SetMapper(self.mapper)

    def set_dims(self,h,r,res=100):
        self.source.SetHeight(h)
        self.source.SetRadius(r)
        self.source.SetResolution(res)
        self.source.Update()

    def set_colour(self,r,g,b):
        self.actor.GetProperty().SetColor(r,g,b)

    def get_actor(self):
        return self.actor

    def set_pos(self,x,y,z):
        self.actor.SetPosition(x,y,z)

    def set_ori(self,a,b,c):
        self.actor.SetOrientation(a,b,c)

    def get_pos(self):
        return self.actor.GetPosition()

    def get_bounds(self):
        return self.actor.GetBounds()

    def get_ori(self):
        return self.actor.GetOrientation()

    def plus_x(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0]+dist,cur_pos[1],cur_pos[2])

    def minus_x(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0]-dist,cur_pos[1],cur_pos[2])

    def plus_y(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0],cur_pos[1]+dist,cur_pos[2])

    def minus_y(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0],cur_pos[1]-dist,cur_pos[2])

    def plus_z(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0],cur_pos[1],cur_pos[2]+dist)

    def minus_z(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0],cur_pos[1],cur_pos[2]-dist)


    def turn_red(self):
        self.actor.GetProperty().SetColor(255,0,0)
    def turn_green(self):
        self.actor.GetProperty().SetColor(0,255,0)
    def turn_blue(self):
        self.actor.GetProperty().SetColor(0,0,255)
    def turn_white(self):
        self.actor.GetProperty().SetColor(255,255,255)
    def turn_silver(self):
        self.actor.GetProperty().SetColor(192,192,192)


class cylinder:
    def __init__(self):
        self.source =  vtk.vtkCylinderSource()

        self.mapper = vtk.vtkPolyDataMapper()
        self.mapper.SetInputConnection(self.source.GetOutputPort())
        self.mapper.Update()

        self.actor=vtk.vtkActor()
        self.actor.SetMapper(self.mapper)

    def set_center(self,x,y,z):
        self.source.SetCenter(x,y,z)
        self.source.Update()

    def set_dims(self,h,r,res=100):
        self.source.SetRadius(r)
        self.source.SetHeight(h)
        self.source.SetResolution(res)
        self.source.Update()

    def set_colour(self,r,g,b):
        self.actor.GetProperty().SetColor(r,g,b)

    def get_actor(self):
            return self.actor

    def set_pos(self,x,y,z):
        self.actor.SetPosition(x,y,z)

    def set_ori(self,a,b,c):
        self.actor.SetOrientation(a,b,c)

    def get_pos(self):
        return self.actor.GetPosition()

    def get_bounds(self):
        return self.actor.GetBounds()

    def get_ori(self):
        return self.actor.GetOrientation()

    def plus_x(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0]+dist,cur_pos[1],cur_pos[2])

    def minus_x(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0]-dist,cur_pos[1],cur_pos[2])

    def plus_y(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0],cur_pos[1]+dist,cur_pos[2])

    def minus_y(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0],cur_pos[1]-dist,cur_pos[2])

    def plus_z(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0],cur_pos[1],cur_pos[2]+dist)

    def minus_z(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0],cur_pos[1],cur_pos[2]-dist)


    def turn_red(self):
        self.actor.GetProperty().SetColor(255,0,0)
    def turn_green(self):
        self.actor.GetProperty().SetColor(0,255,0)
    def turn_blue(self):
        self.actor.GetProperty().SetColor(0,0,255)
    def turn_white(self):
        self.actor.GetProperty().SetColor(255,255,255)
    def turn_silver(self):
        self.actor.GetProperty().SetColor(192,192,192)

class arrow:
    def __init__(self):
        self.source =  vtk.vtkArrowSource()

        self.mapper = vtk.vtkPolyDataMapper()
        self.mapper.SetInputConnection(self.source.GetOutputPort())
        self.mapper.Update()

        self.actor=vtk.vtkActor()
        self.actor.SetMapper(self.mapper)

    def set_center(self,x,y,z):
        self.source.SetCenter(x,y,z)
        self.source.Update()

    def set_dims(self,r,tr,l,sres=100,tres=100):
        self.source.SetShaftRadius(r)
        self.source.SetTipLength(l)    
        self.source.SetTipRadius(tr)    
        self.source.SetShaftResolution(sres)
        self.source.SetTipResolution(tres)
        self.source.Update()

    def set_colour(self,r,g,b):
        self.actor.GetProperty().SetColor(r,g,b)

    def get_actor(self):
            return self.actor

    def set_pos(self,x,y,z):
        self.actor.SetPosition(x,y,z)

    def set_ori(self,a,b,c):
        self.actor.SetOrientation(a,b,c)

    def get_pos(self):
        return self.actor.GetPosition()

    def get_bounds(self):
        return self.actor.GetBounds()

    def get_ori(self):
        return self.actor.GetOrientation()

    def plus_x(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0]+dist,cur_pos[1],cur_pos[2])

    def minus_x(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0]-dist,cur_pos[1],cur_pos[2])

    def plus_y(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0],cur_pos[1]+dist,cur_pos[2])

    def minus_y(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0],cur_pos[1]-dist,cur_pos[2])

    def plus_z(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0],cur_pos[1],cur_pos[2]+dist)

    def minus_z(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0],cur_pos[1],cur_pos[2]-dist)


    def turn_red(self):
        self.actor.GetProperty().SetColor(255,0,0)
    def turn_green(self):
        self.actor.GetProperty().SetColor(0,255,0)
    def turn_blue(self):
        self.actor.GetProperty().SetColor(0,0,255)
    def turn_white(self):
        self.actor.GetProperty().SetColor(255,255,255)
    def turn_silver(self):
        self.actor.GetProperty().SetColor(192,192,192)



class external_graphic:

    def __init__(self,file):
        self.source = vtk.vtkSTLReader()
        self.source.SetFileName(file)
        self.source.Update()

        self.mapper = vtk.vtkPolyDataMapper()
        self.mapper.SetInputConnection(self.source.GetOutputPort())
        self.mapper.Update()

        self.actor = vtk.vtkActor()
        self.actor.SetMapper(self.mapper)

    def set_colour(self,r,g,b):
            self.actor.GetProperty().SetColor(r,g,b)

    def get_actor(self):
            return self.actor

    def set_pos(self,x,y,z):
        self.actor.SetPosition(x,y,z)

    def set_ori(self,a,b,c):
        self.actor.SetOrientation(a,b,c)

    def get_pos(self):
        return self.actor.GetPosition()

    def get_bounds(self):
        return self.actor.GetBounds()

    def get_ori(self):
        return self.actor.GetOrientation()

    def plus_x(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0]+dist,cur_pos[1],cur_pos[2])

    def minus_x(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0]-dist,cur_pos[1],cur_pos[2])

    def plus_y(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0],cur_pos[1]+dist,cur_pos[2])

    def minus_y(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0],cur_pos[1]-dist,cur_pos[2])

    def plus_z(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0],cur_pos[1],cur_pos[2]+dist)

    def minus_z(self,dist):
        cur_pos = self.get_pos()
        self.set_pos(cur_pos[0],cur_pos[1],cur_pos[2]-dist)

    def rotate(self,ang,axis):
        if axis == 0:
            self.actor.RotateWXYZ(ang,1,0,0)
        elif axis == 1:
            self.actor.RotateWXYZ(ang,0,1,0)
        elif axis == 2:
            self.actor.RotateWXYZ(ang,0,0,1)

    def scale(self,x,y,z):
        self.transform = vtk.vtkTransform()
        self.transform.Scale(x,y,z)

        self.transformFilter = vtk.vtkTransformPolyDataFilter()
        self.transformFilter.SetInputConnection(self.source.GetOutputPort())
        self.transformFilter.SetTransform(self.transform)
        self.transformFilter.Update()
        self.mapper.SetInputConnection(self.transformFilter.GetOutputPort())
        self.mapper.Update()

    def turn_red(self):
        self.actor.GetProperty().SetColor(255,0,0)
    def turn_green(self):
        self.actor.GetProperty().SetColor(0,255,0)
    def turn_blue(self):
        self.actor.GetProperty().SetColor(0,0,255)
    def turn_white(self):
        self.actor.GetProperty().SetColor(255,255,255)
    def turn_silver(self):
        self.actor.GetProperty().SetColor(192,192,192)