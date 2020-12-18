import reader_sok as rd
import avatars as av


plan=rd.import_plan_ax('sokoban_plan.csv')



pl1 = av.cube()
pl1.set_dims(1,1,1)

st1 = av.cube()
st1.set_dims(1,1,1)
st1.turn_red()

st2 = av.cube()
st2.set_dims(1,1,1)
st2.turn_blue()

agents = {'player-01':pl1,'stone-01':st1,'stone-02':st2}

def action(plan,agents):
	action = plan[0]
	if action == 'move':
		dirs(plan[4],agents[plan[1]])
	elif action == 'push-to-nongoal':
		dirs(plan[4],agents[plan[1]])
		dirs(plan[4],agents[plan[2]])

	elif action == 'push-to-goal':
		dirs(plan[4],agents[plan[1]])
		dirs(plan[4],agents[plan[2]])

def dirs(direction,actor):
	if direction == 'dir-up':
		actor.plus_y(1)
	elif direction == 'dir-right':
		actor.plus_x(1)
	
	elif direction == 'dir-left':
		actor.minus_x(1)
	
	elif direction == 'dir-down':
		actor.plus_x(1)

c=1
for line in plan:
	action(line,agents)
	print(c,': ',line[0])
	print(agents['player-01'].get_pos())
	print(agents['stone-01'].get_pos())
	print(agents['stone-01'].get_pos())
	c+=1
