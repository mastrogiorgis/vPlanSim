#Jamie Roberts

import csv
import numpy as np

def clean(str):
	commands=[]
	data = []
	data_wash = []
	c = ''
	for char in str:
		if char == '(' or char == ')' or char == 'c':
			pass
		else:
			data.append(char)

	#print(data)
	for char in data:
		if char== ' ':
			data_wash.append(',')
		else:
			data_wash.append(char)
#	print(data_wash)
	for char in data_wash:
		word = False
		if char == ',':
			word = True
			commands.append(c)
		if char == '\n':
			word = True
			commands.append(c)
		elif char != ',':
			word = False
			c += char
		if word == True:
			c=''
#	print(commands)
	return commands

def open_maps(action_ref,action_map,angle_map):

	action_np = np.genfromtxt(action_ref, delimiter = ',',dtype = None, encoding = 'utf8')
	acmap_np = np.genfromtxt(action_map, delimiter = ',')
	angmap_np = np.genfromtxt(angle_map, delimiter = ',')

	return action_np,acmap_np,angmap_np


def check_action_ax(action,action_np,acmap_np,ang_map):

	x_dim = action_np.shape[0]
	y_dim = action_np.shape[1]
	act = -1
	ang = -1
	for i in range(x_dim):
		for j in range(y_dim):
			cond = np.char.equal(action,action_np[i,j])
			if cond == True:
				act = int(acmap_np[i,j])
				ang = int(ang_map[i,j])
			else:
				pass

	return act,ang


def interpet_ax(np_command_list):
	MAX_PLAN_OUTPUT = 22
	plan = np.zeros([len(np_command_list),MAX_PLAN_OUTPUT])
	map,act_map,ang_map=open_maps('action_list.csv','action_code.csv','angle_list.csv')
	angle_mask = []
	j=0
	for i in range(plan.shape[0]):
		for k in range(plan.shape[1]):
			plan[i,k] = -1
	for i in range(len(np_command_list)):
		j=0
		for char in np_command_list[i]:
			if char == '':
				pass
			elif j==0:
				act, ang = check_action_ax(char,map,act_map,ang_map)
				plan[i,j] = act
				angle_mask.append(ang)
				j+=1
			else:
				plan[i,j] = int(char)
				j+=1


	for i in range(plan.shape[0]):
		plan[i,8] = angle_mask[i]

	return plan

def import_plan_ax(filename):

	file = open(filename,'r')
	raw = []
	command_list = []
	with open(filename, mode ='r') as plan:
		reader = csv.reader(plan, delimiter = ' ', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
		for row in plan:
			raw.append(row)
		else:
			pass

	file.close()
	for command in raw:
		command_list.append(clean(command))

	plan = interpet_ax(command_list)

	return plan

#import_plan_ax('ground_plan1.csv')