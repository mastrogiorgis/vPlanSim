"""
@authors G. Mastorakis, B. Lazaruk, J. Roberts
"""

import numpy as np
import vtk

# Constants for use through the project
colours = {
    'extWallInert': (1, 1, 1),
    'intWallInert': (0.95, 0.95, 0.95),
    'obstacleInert': (0.90, 0.90, 0.90),
    'floorInert': (1, .5, .5),
    'extWallGoal': (0.5, 1.5, 0.5),
    'intWallGoal': (0.45, 1.45, 0.45),
    'obstacleGoal': (0.40, 1.40, 0.40),
    'floorGoal': (0.5, 1.0, 0),
    'extWallEntry': (0.5, 0.5, 1.5),
    'intWallEntry': (0.45, 0.45, 1.45),
    'obstacleEntry': (0.40, 0.40, 1.40),
    'floorEntry': (.5, .5, 1),
    'floorElement': (1, 0.7, 0.1),
    'captionColour': (1, 0, 0),
    'floorSelected': (1, 1, 0),
    'wallSelected': (1, 1, 0),
    'pointer': (1, 1, 0)
}

# Don't reduce the wallY without correcting the functions that determine if an actor is a wall by its height
dimensions = {
    'wallX': 0.99,
    'wallY': 1.0,
    'wallZ': 0.99,
    'floorX': 0.99,
    'floorY': 0.001,
    'floorZ': 0.99
}

opacities = {
    'floor': 1.0,
    'cube': 1.0,
    'transparent': 0.05,
    'opaque': 1.0
}


class points(vtk.vtkPoints):

    def __init__(self):
        pass

    def populate(self,pData):
        for i in range(pData.shape[0]):
            try:
                self.add_point(pData[i])
            except:
                pass
    def add_point(self,pObj):
        self.InsertNextPoint(pObj)

class glyph(vtk.vtkVertexGlyphFilter):

    def __init__(self,polydata):
        self.AddInputData(polydata)
        self.Update()

class d_struc(vtk.vtkPolyData):

    def __init__(self,points):
        self.SetPoints(points)

class actor(vtk.vtkActor):

    def __init__(self,data):
        self.SetMapper(data)

    def Rotate(self,x,y,z):
        self.RotateX(-45)
        self.RotateY(0)
        self.RotateZ(45)

class mapper(vtk.vtkPolyDataMapper):

    def __init__(self,data,dtype = False):
        if dtype:
            self.SetInputConnection(data)
        else:
            self.SetInputData(data)

def pointer(x, y, z, radius):
    # cast the positions to text so they can be added as labels
    labelX = str(x)
    labelY = str(y)
    labelZ = str(z)

    # Create sphere
    sphere_source = vtk.vtkSphereSource()
    sphere_source.SetCenter(x, y, z)
    sphere_source.SetRadius(radius)
    sphere_source.Update()

    # Create the caption to show the sphere position
    caption = vtk.vtkCaptionActor2D()
    caption.SetCaption("(" + labelX + ", " + labelY + ", " + labelZ + ")")

    # Set the size of the caption box. The box is measured from the lower left corner to the upper right corner.
    # SetWidth and SetHeight are defined as fraction of the viewport.  So SetWidth(0.1) sets the caption box
    # to 10% the width of the viewport.
    # The caption text will then fill the provided caption box as best possible
    caption.SetWidth(0.15)
    caption.SetHeight(0.02)

    caption.GetProperty().SetColor(colours['captionColour'])
    caption.SetAttachmentPoint(sphere_source.GetCenter())

    # Formatting of the text possible with vtkTextProperty
    # Disable the border box for the caption
    caption.BorderOff()

    # Map texture coordinates of the cube_source
    map_to_plane = vtk.vtkTextureMapToPlane()
    map_to_plane.SetInputConnection(sphere_source.GetOutputPort())

    # Create polydatamapper and set the mapped texture as input
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(map_to_plane.GetOutputPort())
    # Create actor and set the mapper and the texture . uncomment if no texture
    #  mapper = vtk.vtkPolyDataMapper()
    # mapper.SetInputConnection(cube_source.GetOutputPort())
    mapper.Update()

    # create the sphere actor with the mapper
    sphere = vtk.vtkActor()
    sphere.SetMapper(mapper)
    sphere.GetProperty().SetColor(colours['pointer'])

    # Assemble the cube and annotations into a complete prop actor.
    pointer = vtk.vtkPropAssembly()
    pointer.AddPart(sphere)
    pointer.AddPart(caption)

    # actor.SetTexture(texture)

    return pointer

def cube_from_source(x, y, z, visibility, colour, transparency):
    # img = 'OIZV2N0.jpg'

    # Cast the positions to text so they can be added as labels
    labelX = str(x)
    # labelY = str(y)  # We're not displaying the y-position anymore
    labelZ = str(z)

    # Create cube
    cube_source = vtk.vtkCubeSource()
    cube_source.SetCenter(x, y, z)
    cube_source.SetXLength(dimensions['wallX'])
    cube_source.SetYLength(dimensions['wallY'])
    cube_source.SetZLength(dimensions['wallZ'])
    cube_source.Update()

    # Create the caption to show the cube position
    # caption = vtk.vtkCaptionActor2D()
    # caption.SetCaption("(" + labelX + ", " + labelY + ", " + labelZ + ")")
    # caption.SetCaption("(" + labelX + ", " + labelZ + ")")

    # Set the size of the caption box. The box is measured from the lower left corner to the upper right corner.
    # SetWidth and SetHeight are defined as fraction of the viewport.  So SetWidth(0.1) sets the caption box
    # to 10% the width of the viewport.
    # The caption text will then fill the provided caption box as best possible
    # caption.SetWidth(0.15)
    # caption.SetHeight(0.02)
    #
    # caption.GetProperty().SetColor(colours['captionColour'])
    # caption.SetAttachmentPoint(cube_source.GetCenter())

    # Formatting of the text possible with vtkTextProperty
    # Disable the border box for the caption
    # caption.BorderOff()

    # Set the initial visiblity of the caption
    # if visibility == False:
    #     caption.GetCaptionTextProperty().SetOpacity(0)
    #     caption.LeaderOff()

    # read image
    # reader = vtk.vtkJPEGReader()
    # reader.SetFileName(img)

    # Create texture object from image
    # texture = vtk.vtkTexture()
    # texture.SetInputConnection(reader.GetOutputPort())

    # Map texture coordinates of the cube_source
    # map_to_plane = vtk.vtkTextureMapToPlane()
    # map_to_plane.SetInputConnection(cube_source.GetOutputPort())

    # Create polydatamapper and set the mapped texture as input
    # mapper = vtk.vtkPolyDataMapper()
    # mapper.SetInputConnection(map_to_plane.GetOutputPort())
    # Create actor and set the mapper and the texture . uncomment if no texture
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(cube_source.GetOutputPort())
    mapper.Update()

    # create the cube actor with the mapper
    cube = vtk.vtkActor()
    cube.SetMapper(mapper)
    cube.GetProperty().SetColor(colours[colour])
    if transparency == True:
        cube.GetProperty().SetOpacity(opacities['transparent'])
    else:
        cube.GetProperty().SetOpacity(opacities['opaque'])

    # Assemble the cube and annotations into a complete prop actor.
    actor = vtk.vtkPropAssembly()
    actor.AddPart(cube)
    # actor.AddPart(caption)
    # actor.RemovePart(caption)
    return actor

def floor_panel(origin, w, l):
    cube_source = vtk.vtkCubeSource()

    cube_source.SetCenter(origin[0], origin[1], origin[2])
    cube_source.SetXLength(dimensions['floorX'])
    cube_source.SetYLength(dimensions['floorY'])
    cube_source.SetZLength(dimensions['floorZ'])
    cube_source.Update()

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(cube_source.GetOutputPort())
    mapper.Update()

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colours['floorInert'])
    actor.GetProperty().SetOpacity(opacities['floor'])

    return actor

def insert_plane():
    img = 'floor.jpg'
    cube_source = vtk.vtkCubeSource()

    cube_source.SetCenter(0.49, 10, 10)
    cube_source.SetXLength(0.0010)
    cube_source.SetYLength(20)
    cube_source.SetZLength(20)
    cube_source.Update()

    reader = vtk.vtkJPEGReader()
    reader.SetFileName(img)

    # Create texture object
    texture = vtk.vtkTexture()
    texture.SetInputConnection(reader.GetOutputPort())

    # Map texture coordinates
    map_to_plane = vtk.vtkTextureMapToPlane()
    map_to_plane.SetInputConnection(cube_source.GetOutputPort())

    # Create mapper and set the mapped texture as input
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(map_to_plane.GetOutputPort())

    # Create actor and set the mapper and the texture . uncomment if no texture

    #  mapper = vtk.vtkPolyDataMapper()
    # mapper.SetInputConnection(cube_source.GetOutputPort())
    mapper.Update()

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.SetTexture(texture)
    return actor

def structured_grid_2(lx, ly, lz, space):
    nx = int((lx / space))
    ny = int((ly / 0.1))
    nz = int((lz / space))
    x_r = np.linspace(-lx, lx, nx)
    y_r = np.linspace(-ly, ly, ny)
    z_r = np.linspace(-lz, lz, nz)
    point = points()
    #
    for i in range(x_r.shape[0]):
        for j in range(y_r.shape[0]):
            for k in range(z_r.shape[0]):
                point.InsertNextPoint(x_r[i], y_r[j], z_r[k])

    polydata = d_struc(point)
    glyph_obj = glyph(polydata)
    mapper_obj = mapper(glyph_obj.GetOutputPort(), dtype=True)
    actor_obj = actor(mapper_obj)
    actor_obj.GetProperty().SetPointSize(1)
    actor_obj.SetPosition(0, 0, 0)
    return actor_obj

class strut:

    def __init__(self):
        self.pos = np.array([0,0,0])
        self.point_a = np.array([0,0,0])
        self.point_b = np.array([1,0,0])
        self.point_c = np.array([0,0,1])
        self.point_d = np.array([1,0,1])

        self.point_e = np.array([0,4,0])
        self.point_f = np.array([1,4,0])
        self.point_g = np.array([0,4,1])
        self.point_h = np.array([1,4,1])


        self.v_points = vtk.vtkPoints()
        self.v_points.InsertNextPoint(self.point_a)
        self.v_points.InsertNextPoint(self.point_b)
        self.v_points.InsertNextPoint(self.point_c)
        self.v_points.InsertNextPoint(self.point_d)

        self.v_points.InsertNextPoint(self.point_e)
        self.v_points.InsertNextPoint(self.point_f)
        self.v_points.InsertNextPoint(self.point_g)
        self.v_points.InsertNextPoint(self.point_h)

        line = vtk.vtkLine()
        line.GetPointIds().SetId(0, 0);
        line.GetPointIds().SetId(1, 1);

        self.cellArray = vtk.vtkCellArray()

        #self.cellArray.InsertNextCell(line);

        #face1
        self.cellArray.InsertNextCell(3)
        self.cellArray.InsertCellPoint(0)
        self.cellArray.InsertCellPoint(1)
        self.cellArray.InsertCellPoint(2)
        #face2
        self.cellArray.InsertNextCell(3)
        self.cellArray.InsertCellPoint(2)
        self.cellArray.InsertCellPoint(3)
        self.cellArray.InsertCellPoint(1)
        #face3
        self.cellArray.InsertNextCell(3)
        self.cellArray.InsertCellPoint(4)
        self.cellArray.InsertCellPoint(5)
        self.cellArray.InsertCellPoint(6)
        #face4
        self.cellArray.InsertNextCell(3)
        self.cellArray.InsertCellPoint(5)
        self.cellArray.InsertCellPoint(6)
        self.cellArray.InsertCellPoint(7)
        #face5
        self.cellArray.InsertCellPoint(3)
        self.cellArray.InsertCellPoint(7)
        self.cellArray.InsertNextCell(3)
        self.cellArray.InsertCellPoint(2)
        #face6
        self.cellArray.InsertNextCell(3)
        self.cellArray.InsertCellPoint(7)
        self.cellArray.InsertCellPoint(6)
        self.cellArray.InsertCellPoint(2)
        #face7
        self.cellArray.InsertNextCell(3)
        self.cellArray.InsertCellPoint(1)
        self.cellArray.InsertCellPoint(5)
        self.cellArray.InsertCellPoint(3)
        #face8
        self.cellArray.InsertNextCell(3)
        self.cellArray.InsertCellPoint(5)
        self.cellArray.InsertCellPoint(7)
        self.cellArray.InsertCellPoint(3)
        #face9
        self.cellArray.InsertNextCell(3)
        self.cellArray.InsertCellPoint(0)
        self.cellArray.InsertCellPoint(5)
        self.cellArray.InsertCellPoint(1)
        #face10
        self.cellArray.InsertNextCell(3)
        self.cellArray.InsertCellPoint(5)
        self.cellArray.InsertCellPoint(4)
        self.cellArray.InsertCellPoint(1)
        #face11
        self.cellArray.InsertNextCell(3)
        self.cellArray.InsertCellPoint(0)
        self.cellArray.InsertCellPoint(4)
        self.cellArray.InsertCellPoint(2)
        #face12
        self.cellArray.InsertNextCell(3)
        self.cellArray.InsertCellPoint(4)
        self.cellArray.InsertCellPoint(6)
        self.cellArray.InsertCellPoint(2)

        self.polydata = vtk.vtkPolyData()
        self.polydata.SetPoints(self.v_points)
        self.polydata.SetPolys(self.cellArray)

        self.mapper = vtk.vtkPolyDataMapper()
        self.mapper.SetInputData(self.polydata)

        self.actor = vtk.vtkActor()
        self.actor.SetMapper(self.mapper)

    def normalise(self,x,y,z):
        return x+0.5, y+0.5, z+0.5

    def tag(self,t_id):
        self.id = t_id

    def get_tag(self,t_id):
        try:
            return self.id
        except:
            print('actor not tagged')
            return 1

    def get_actor(self):
        return self.actor

    def set_pos(self,x,y,z):
        xi,yi,zi = self.normalise(x,y,z)
        self.actor.SetPosition(xi,yi,zi)

    def set_ori(self,a,b,c):
        self.actor.SetOrientation(a,b,c)

    def get_pos(self):
        return self.actor.GetPosition()

    def get_bounds(self):
        return self.actor.GetBounds()

    def get_ori(self):
        return self.actor.GetOrientation()

    def get_rot_mat_x(self,theta):
        mat = np.array([[1,0,0],[0,np.cos(theta),-np.sin(theta)],[0,np.sin(theta),np.cos(theta)]])
        return mat

    def get_rot_mat_y(self,theta):
        mat = np.array([[np.cos(theta),0,np.sin(theta)],[0,1,0],[-np.sin(theta),0,np.cos(theta)]])
        return mat

    def get_rot_mat_z(self,theta):
        mat = np.array([[np.cos(theta),-np.sin(theta),0],[np.sin(theta),np.cos(theta),0],[0,0,1]])
        return mat

    def turn_texture(self):
        self.reader = vtk.vtkJPEGReader()
        self.reader.SetFileName('blue.jpg')
        # Create texture object
        self.texture = vtk.vtkTexture()
        self.texture.SetInputConnection(self.reader.GetOutputPort())

        self.textureCoordinates = vtk.vtkFloatArray();
        self.textureCoordinates.SetName("TextureCoordinates")
        self.textureCoordinates.SetNumberOfComponents(3)

        tuple = [0.0, 0.0, 0.0]
        self.textureCoordinates.InsertNextTuple(tuple)
        tuple[0] = 1.0
        tuple[1] = 1.0
        tuple[2] = 1.0
        self.textureCoordinates.InsertNextTuple(tuple)
        tuple[0] = 1.0
        tuple[1] = 1.0
        tuple[2] = 5.0
        self.textureCoordinates.InsertNextTuple(tuple)
        tuple[0] = 2.0
        tuple[1] = 2.0
        tuple[2] = 2.0
        self.textureCoordinates.InsertNextTuple(tuple)
        self.polydata.GetPointData().SetTCoords(self.textureCoordinates);

        #Map texture coordinates
        #map_to_plane = vtk.vtkTextureMapToPlane()
        #map_to_plane.SetInputConnection(self.polydata())

        # Create mapper and set the mapped texture as input
        self.mapper = vtk.vtkPolyDataMapper()
        self.mapper.SetInputData(self.polydata)
        self.actor.SetMapper(self.mapper)
        self.actor.SetTexture(self.texture)


def gen_struts(n_struts):
    strut_list = []
    for i in range(n_struts):
        strut_list.append(cs.strut())

    return strut_list