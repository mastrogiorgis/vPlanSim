#Jamie Roberts

import vis as graphics
import numpy as np
import reader as rd
import process_action as ac
import argparse

##THIS VISUALISATIOJN IS DRIVEN BY USER INTERACTION. PRESS 'Q' TO LOOP TO THE NEXT STEP OF THE PLAN

parser = argparse.ArgumentParser()
parser.add_argument("file", help= "plan to simulate as a .csv type")
args = parser.parse_args()
file = "{}".format(args.file)

#import the raw plan from csv file
plan1 = rd.read_plan(file)

#process raw plan input into actions for visualisation
win = graphics.initialise_graphics()

agent1 = graphics.strut()
agent1.actor.GetProperty().SetColor(0.8,0,0)

stone1 = graphics.strut()
stone1.actor.GetProperty().SetColor(0,0.8,0)

stone2 = graphics.strut()
stone2.actor.GetProperty().SetColor(0,0,0.8)

agent1.set_pos(0,5,5)

stone1.set_pos(0,3,3)

stone2.set_pos(0,4,4)

order = ac.find_order(plan1)

graphics.add_strut(win,agent1)
graphics.add_strut(win,stone1)
graphics.add_strut(win,stone2)

#reset camera for view of environment
win.ren.ResetCamera()
win.ren.GetActiveCamera().SetFocalPoint(1.0,8.0,4.0)
win.ren.GetActiveCamera().SetPosition(10,0,-10)
win.ren.GetActiveCamera().SetViewUp(1.0,0.0,0.0)
win.update()
def get_instructions(plan):
	agents=[]
	directions=[]

	if plan[0] == 'move':
		if plan[1] == 'player-01':
			agents.append(agent1)
		if plan[4] == 'dir-up':
			directions.append([0,0,1])
		if plan[4] == 'dir-down':
			directions.append([0,0,-1])
		if plan[4] == 'dir-left':
			directions.append([0,-1,0])
		if plan[4] == 'dir-right':
			directions.append([0,1,0])

	elif plan[0] == 'push-to-nongoal':
		if plan[1] == 'player-01':
			agents.append(agent1)
		if plan[2] == 'stone-01':
			agents.append(stone1)
		if plan[2] == 'stone-02':
			agents.append(stone2)
		if plan[6] == 'dir-up':
			directions.append([0,0,1])
		if plan[6] == 'dir-down':
			directions.append([0,0,-1])
		if plan[6] == 'dir-left':
			directions.append([0,-1,0])
		if plan[6] == 'dir-right':
			directions.append([0,1,0])

	elif plan[0] == 'push-to-goal':
		if plan[1] == 'player-01':
			agents.append(agent1)
		if plan[2] == 'stone-01':
			agents.append(stone1)
		if plan[2] == 'stone-02':
			agents.append(stone2)
		if plan[6] == 'dir-up':
			directions.append([0,0,1])
		if plan[6] == 'dir-down':
			directions.append([0,0,-1])
		if plan[6] == 'dir-left':
			directions.append([0,-1,0])
		if plan[6] == 'dir-right':
			directions.append([0,1,0])

	return agents,directions


c=1
for p in plan1:
	a,d = get_instructions(p)
	print(a)
	c+=1
	ac.do_action(p[0],a,d)
	win.update()