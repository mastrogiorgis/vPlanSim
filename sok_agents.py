import vtk
import numpy as np

class strut:
    
	def __init__(self):
    	
		self.pos = np.array([0,0,0])
		self.point_a = np.array([0,0,0])
		self.point_b = np.array([1,0,0])
		self.point_c = np.array([0,0,1])
		self.point_d = np.array([1,0,1])

		self.point_f = np.array([1,1,0])
		self.point_g = np.array([0,1,1])
		self.point_h = np.array([1,1,1])

		self.point_e = np.array([0,1,0])
		self.v_points = vtk.vtkPoints()
		self.v_points.InsertNextPoint(self.point_a)
		self.v_points.InsertNextPoint(self.point_b)
		self.v_points.InsertNextPoint(self.point_c)
		self.v_points.InsertNextPoint(self.point_d)

		self.v_points.InsertNextPoint(self.point_e)
		self.v_points.InsertNextPoint(self.point_f)
		self.v_points.InsertNextPoint(self.point_g)
		self.v_points.InsertNextPoint(self.point_h)

		self.cellArray = vtk.vtkCellArray()
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

	def turn_red(self):
		self.actor.GetProperty().SetColor(255,0,0)
	def turn_green(self):
		self.actor.GetProperty().SetColor(0,255,0)
	def turn_blue(self):
		self.actor.GetProperty().SetColor(0,0,255)
	def turn_white(self):
		self.actor.GetProperty().SetColor(255,255,255)
