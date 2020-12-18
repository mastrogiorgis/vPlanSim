#Jamie Roberts

import numpy as np
import csv


def process_acts(act):
    action = act[0]

    if action == 1:

        x1 = act[1]

        y1 = act[2]

        z1 = act[3]

        p1 = act[4]
        p2 = act[5]
        p3 = act[6]

        a_fr = 0
        a_to = 0
        instruction = np.array([action,x1,y1,z1,p1,p2,p3,a_fr,a_to])

    else:

        x1 = act[1]
        x2 = act[4]

        y1 = act[2]
        y2 = act[5]

        z1 = act[3]
        z2 = act[6]

        a_fr = act[7]
        a_to = act[8]
        instruction = np.array([action,x1,y1,z1,x2,y2,z2,a_fr,a_to])

    return instruction

def action_list_ax(act,strut):

    if act[0] == 1:
        x = act[1]
        y = act[2]
        z = act[3]
        a = act[8]

        if a == 0:
            text = 'insert'
            strut.set_ori(0,0,0)
            strut.set_pos(x,z,y)
 
        elif a == 90:
            text = 'insert'
            strut.set_ori(a,0,0)
            strut.set_pos(x,z,y)

        elif a == 450:
            text = 'insert'
            strut.set_ori(0,0,at)
            strut.set_pos(x-1.5,z+1.5,y)

        return text,z,x,y

    elif act[0] == 2:
        x = act[4]
        y = act[5]
        z = act[6]
        af = act[7]
        at = act[8]

        if  at == 90:
            text = 'rad2'
            strut.set_ori(0,at,0)
            strut.set_pos(x-1.5,z,y+1.5)

        elif at == 0:
            text = 'rad2'
            strut.set_ori(0,0,0)
            strut.set_pos(x,z,y)

        return text,z,x,y

    elif act[0] == 3:
        x = act[4]
        y = act[5]
        z = act[6]
        at = act[8]

        if at == 0:
            text = 'walk_forward'
            strut.set_ori(0,0,0)
            strut.set_pos(x,z,y)

        elif at == 90:
            text = 'walk_forward'
            strut.set_ori(0,at,0)
            strut.set_pos(x-1.5,z,y+1.5)

        elif at == 450:
            text = 'walk_forward'
            strut.set_ori(0,0,at)
            strut.set_pos(x-1.5,z+1.5,y)

        return text,z,x,y

    elif act[0] == 4:
        x = act[4]
        y = act[5]
        z = act[6]
        at = act[8]

        if at == 0:
            text = 'walk_backwards'
            strut.set_ori(0,0,0)
            strut.set_pos(x,z,y)

        elif at == 90:
            text = 'walk_backwards'
            strut.set_ori(0,at,0)
            strut.set_pos(x-1.5,z,y+1.5)

        elif at == 450:
            text = 'walk_backward'
            strut.set_ori(0,0,at)
            strut.set_pos(x-1.5,z+1.5,y)

        return text, z,x,y

    elif act[0] == 5:
        x = act[4]
        y = act[5]
        z = act[6]
        af = act[7]
        at = act[8]

        if  at == 90:
            text = 'rax'
            strut.set_ori(0,at,0)
            strut.set_pos(x-1.5,z,y+1.5)

        elif at == 0:
            text = 'rax'
            strut.set_ori(0,0,0)
            strut.set_pos(x,z,y)

        return text,z,x,y

    elif act[0] == 6:
        x = act[4]
        y = act[5]
        z = act[6]
        af = act[7]
        at = act[8]

        if at == 0:
            text = 'swing'
            strut.set_ori(0,0,0)
            strut.set_pos(x,z,y)

        elif at == 90:
            text = 'swing'
            strut.set_ori(0,at,0)
            strut.set_pos(x-1.5,z,y+1.5)
##  FOR XZY
        elif at == 450:
            text = 'swing'
            strut.set_ori(0,0,at)
            strut.set_pos(x-1.5,z+1.5,y)


        return text,z,x,y

    elif act[0] == 7:

        x = act[4]
        y = act[5]
        z = act[6]
        af = act[7]
        at = act[8]

        if at == 450:
            text = 'rd1'
            strut.set_ori(0,0,at)
            strut.set_pos(x-1.5,z+1.5,y)

        elif at == 0:
            text = 'rd1'
            strut.set_ori(0,0,0)
            strut.set_pos(x,z,y)

        else:
            text = 'rd1 error'
        return text,z,x,y

    elif act[0] == 8:
        x = act[4]
        y = act[5]
        z = act[6]
        af = act[7]
        at = act[8]


        if at == 0:
            text = 'rd15'
            strut.set_ori(0,0,0)
            strut.set_pos(x,z,y)

        elif at == 90:
            text = 'rd15'
            strut.set_ori(0,at,0)
            strut.set_pos(x-1.5,z,y+1.5)

        else:
            text = 'rd15 error'
        return text,z,x,y

    elif act[0] == 9:

        x = act[4]
        y = act[5]
        z = act[6]
        at = act[8]

        if at == 0:
            text = 'radwn'
            strut.set_ori(0,0,0)
            strut.set_pos(x,z,y)

        elif at == 90:
            text = 'radwn'
            strut.set_ori(0,at,0)
            strut.set_pos(x-1.5,z,y+1.5)

        else:
            text = 'radwn error'

#    return text
        return text, z,x,y

def find_order(x,y,z,order,i,plan):

    while i >= 0:
        if plan[i,0] != 1:
            check_x = plan[i,4]
            check_y = plan[i,5]
            check_z = plan[i,6]
            if x == check_x and y == check_y and z == check_z:
                val = order[i,0]
                break
        elif plan[i,0] == 1:
            check_x = plan[i,1]
            check_y = plan[i,2]
            check_z = plan[i,3]
            if x == check_x and y == check_y and z == check_z:
                val = order[i,0]
                break

        else:
            print('pass case')
            pass
        i = i - 1

    return val



def gen_order(plan):
    length = plan.shape[0]
    order = np.ones([length,1])
    order[:,:] = -1
    strut = -1

    for i in range(plan.shape[0]):

        if plan[i,0] == 1:

            strut += 1
            order[i,0] = strut
            curr_strut = strut
        elif plan[i,0] != 1:

            if plan[i-1,0] == 1:

                old_x = plan[i-1,1]
                old_y = plan[i-1,2]
                old_z = plan[i-1,3]

            elif plan[i-1,0] != 1:

                old_x = plan[i-1,4]
                old_y = plan[i-1,5]
                old_z = plan[i-1,6]

            if old_x == plan[i,1] and old_y == plan[i,2] and old_z == plan[i,3]:
                order[i,0] = curr_strut

            else:

                x = plan[i,1]
                y = plan[i,2]
                z = plan[i,3]


                curr_strut = find_order(x,y,z,order,i,plan)
                order[i,0] = curr_strut

                old_x = plan[i,4]
                old_y = plan[i,5]
                old_z = plan[i,6]

        else:
            old_x = plan[i,1]
            old_y = plan[i,2]
            old_z = plan[i,3]

    return order

def get_n_struts(plan):
    s_count = 0
    for i in range(plan.shape[0]):
        if plan[i,0] == 1:
            s_count+=1
        else:
            pass
    return s_count