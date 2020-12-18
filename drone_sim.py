#Jamie Roberts

import csv
import numpy as np
import avatars as av

def read_plan(file):
	with open(file,mode = 'r') as csv_file:

		csv_reader = csv.reader(csv_file)
		read = []
		for row in csv_reader:
			for line in row:
				#do all text cleaning here
				line = line.replace('(','')
				line = line.replace(')','')
				line = line.replace(' ',',')
#				line = line.replace('c','')

				#split plan into list when text is clean
				read_line = line.split(',')
				read.append(read_line)

	return read


def clean(str):
	commands=[]
	data = []
	data_wash = []
	c = ''
	for char in str:
		if char == '(' or char  == ')':
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
	return commands


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
	plan = command_list
#	plan = interpet_ax(command_list)
	return plan


def get_int(text,switch):
    if switch == 'agent':
        integer = text.replace('s','')
        return int(integer)
    else:
        integer = text.replace('c','')
        return int(integer)

def gen_drones(nDrones):
    d = []

    for i in range(nDrones):
        drone = av.external_graphic('drone.stl')
        drone.scale(0.08,0.08,0.08)
        drone.set_colour(0.2,0.8,0)
        drone.rotate(90,0)
        d.append(drone)

    return d


def action(plan,drone):
    print(plan)
    action = plan[0]
    if action == 'insert':
        dr_index = get_int(plan[1],'agent')
        x=get_int(plan[2],'pos')
        y=get_int(plan[3],'pos')
        z=get_int(plan[4],'pos')
        drone[dr_index].set_pos(x,z,y)

    elif action == 'walk_plusx':
        dr_index = get_int(plan[1],'agent')
        drone[dr_index].plus_x(1)

    elif action == 'walk_minusx':
        dr_index = get_int(plan[1],'agent')
        drone[dr_index].plus_x(1)

    elif action == 'walk_plusy':
        dr_index = get_int(plan[1],'agent')
        drone[dr_index].plus_y(1)

    elif action == 'walk_minusy':
        dr_index = get_int(plan[1],'agent')
        drone[dr_index].minus_y(1)

    elif action == 'walk_plusz':
        dr_index = get_int(plan[1],'agent')
        drone[dr_index].plus_z(1)

    elif action == 'walk_minusz':
        dr_index = get_int(plan[1],'agent')
        drone[dr_index].minus_z(1)
