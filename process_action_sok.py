#Jamie Roberts

import numpy as np
import csv

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

def check_player(plan):
	action = plan[0]
	print(action)
	if action == 'move':
		return plan[1]
	elif action == 'push-to-nongoal':
		return plan[2]
	elif action == 'push-to-goal':
		return plan[2]
    
def get_init_pos(plan):
	action = plan[0]
	if action == 'move':
		x,y= get_integers(plan[2])
	elif action == 'push-to-nongoal':
		x,y= get_integers(plan[4])
	elif action == 'push-to-goal':
		x,y= get_integers(plan[4])
	else:
		x=0
		y=0
	return x,y

def get_integers(string):
	ints = []
	for s in string:
		try:
			ints.append(int(s))
		except:
			pass
	x = ints[0]
	y = ints[1]
	return x,y

def interpret_initial_pos(agent,plan):
	players = []
	for r in plan:
		pl = check_player(r)
		if pl in players:
			pass
		else:
			x,z=get_init_pos(r)
			agent[pl].set_pos(x,0,z)
			players.append(pl)

def do_action(cmd,agents,directions):

	if cmd == 'move':
		cur_pos = agents[0].get_pos()
		z = cur_pos[0]+directions[0][0]
		x = cur_pos[1]+directions[0][1]
		y = cur_pos[2]+directions[0][2]
		agents[0].set_pos(z,x,y)

	elif cmd == 'push-to-nongoal':
		cur_pos = agents[0].get_pos()
		cur_pos_stone = agents[1].get_pos()
		z = cur_pos[0]+directions[0][0]
		x = cur_pos[1]+directions[0][1]
		y = cur_pos[2]+directions[0][2]

		z_s = cur_pos_stone[0]+directions[0][0]
		x_s = cur_pos_stone[1]+directions[0][1]
		y_s = cur_pos_stone[2]+directions[0][2]

		agents[0].set_pos(z,x,y)
		agents[1].set_pos(z_s,x_s,y_s)

	elif cmd == 'push-to-goal':
		cur_pos = agents[0].get_pos()
		cur_pos_stone = agents[1].get_pos()
		z = cur_pos[0]+directions[0][0]
		x = cur_pos[1]+directions[0][1]
		y = cur_pos[2]+directions[0][2]

		z_s = cur_pos_stone[0]+directions[0][0]
		x_s = cur_pos_stone[1]+directions[0][1]
		y_s = cur_pos_stone[2]+directions[0][2]


		agents[0].set_pos(z,x,y)
		agents[1].set_pos(z_s,x_s,y_s)
	
	else:
		print('no such action')

def find_order(plan):
	order = []
	for p in plan:
		if p[0] == 'move':
			order.append([p[1]])
		else:
			order.append([p[1],p[2]])

	return order


def action(plan,agents):
	action = plan[0]
	print(plan)
	if action == 'move':
		dirs(plan[4],agents[plan[1]])
	elif action == 'push-to-nongoal':
		dirs(plan[6],agents[plan[1]])
		dirs(plan[6],agents[plan[2]])
	elif action == 'push-to-goal':
		dirs(plan[6],agents[plan[1]])
		dirs(plan[6],agents[plan[2]])

def dirs(direction,actor):
	if direction == 'dir-up':
		actor.minus_z(1)
	elif direction == 'dir-right':
		actor.plus_x(1)
	elif direction == 'dir-left':
		actor.minus_x(1)
	elif direction == 'dir-down':
		actor.plus_z(1)
