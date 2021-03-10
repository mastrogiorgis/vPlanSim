# -*- coding: utf-8 -*-
"""
Created on Tues 1 Dec

@author: Santiago Franco

Define Derived Drone problem
"""

import numpy as np

class drone():
    def __init__(self):
        pass

    def generatePDDLproblem(self, domain, problemName, wallcoords, elements, entries, goal_data):
        print('Drone called\n')
        # get the maximum value of X,Y,Z coordinates to be used for the coord and plus* parameters
        maxOfCoods = np.max(wallcoords) + 1 # add 1 to be inclusive of the max coordinate used later in the for loops
        
        #print("coords = ", maxOfCoods)
        #print("walls = ", wallcoords)
        
        problem_file_name='problem_' + problemName+".pddl"
        exp = "{}".format(problem_file_name)
        problem = open(exp,"w")
        problem.write("(define (problem " + problemName + ") (:domain " + domain + ")\n")
        
        problem.write('(objects: \n\t\t')
        for pos in range(maxOfCoods):
            #print(pos)
            problem.write("c%d "%pos)
        problem.write(" - coord\n")
        problem.write(")\n")
        problem.write("(:init\n\t\t")

        for coord in range(maxOfCoods-1):
            to_coord=coord+1
            problem.write("(plus_one c%i c%i) "%(coord,to_coord))
        problem.write("\n\t\t")

        for coord in range(maxOfCoods-3):
            to_coord=coord+3
            problem.write("(plus_three c%i c%i) "%(coord,to_coord))
        problem.write("\n\t\t")

        for coord in range(maxOfCoods-4):
            to_coord=coord+4
            problem.write("(plus_four c%i c%i) "%(coord,to_coord))
        problem.write("\n\n\t\t")


        for i in range(len(entries)):
            x, y, z = entries[i][0], entries[i][1], entries[i][2] # the plus 1 is to have the aperture at 2 blocks tall
            problem.write('\t(at_aperture c{} c{} c{}) \n\n'.format(x, y, z))



        for var in range(elements):
            problem.write("\t\t(at_agent s%i outC outC outC)\n"%var)
        #problem.write("\t(at_agent1 s%i c0 c0 c1)\n"%(agents-2))
        #problem.write("\t(at_agent2 s%i c1 c0 c1)\n"%(agents-2))
        #problem.write("\t(at_agent3 s%i c2 c0 c1)\n"%(agents-2))
        #problem.write("\t(at_agent4 s%i c3 c0 c1)\n"%(agents-2))
        #problem.write("\t(angle_agent s%i 0ang)\n"%(agents-1))

        #closing init
        problem.write(")\n")

        problem.write("(:goal  (and\n")
        #problem.write("\t(at_agent s%i c0 c0 c1)\n"%(agents-1))a
        #for var in range(agents):
        for i in range(len(goal_data)):
            #problem.write("\t(at_agent s%i c%i c%i c%i)\n"%(var,goalX,goalY,goalZ))
            x, y, z = goal_data[i][0], goal_data[i][1], goal_data[i][2]
            problem.write('\t\t(at_agent s{} c{} c{} c{}) '.format(i,x, y, z))

        problem.write("))\n")
        problem.write(")\n")
        problem.close()
     
    # # load up the predicates and objects with values by iterating through the lists of scene coords, goals and struts
    # def addVars(self, listA, strA):
    #     strB = ''
    #     if strA == 'stat_at':
    #         for i in range(len(listA)): # comm
    #             x,y,z = listA[i][0], listA[i][1], listA[i][2]
    #             strB += ('(stat_at {}c {}c {}c) '.format(x,y,z))
    #     elif strA == 'goal':
    #         strB = '\t(:goal  (and \n'
    #         for i in range(len(listA)):
    #             x, y, z, a = listA[i][0], listA[i][1], listA[i][2], listA[i][3]
    #             strB += ('\t\t(at_agent {}c {}c {}c) '.format(x, y, z))
    #         strB += '\n\t\t) \n\t) \n)'
    #     elif strA == 'aperture':
    #         for i in range(len(listA)):
    #             x, y, z, a = listA[i][0], listA[i][1]+1, listA[i][2], listA[i][3] # the plus 1 is to have the aperture at 2 blocks tall
    #             strB += ('\t\t(at_aperture {}c {}c {}c) \n'.format(x, y, z))
    #     elif strA == 'drones':
    #          for i in range(len(entries)):
    #             strB += ('\t\t(at_agent s%i outC outC outC) \n')
    #     elif strA == 'dyn_at':
    #         for i in range(len(listA)):
    #             strB += '\t\t'
    #             for j in range(4): # iterate to get +1 in either x or z - an if statement will be required here
    #                 x, y, z = listA[i][0]+j, listA[i][1], listA[i][2] 
    #                 strB += ('(dyn_at {}c {}c {}c)'.format(x, y, z))
    #             strB += '\n'
    #     elif all(x in strA for x in 'plus'):
    #         for i in range(len(listA)):
    #             k, j = listA[i][0], listA[i][1]
    #             strB += ('('+strA+ ' {}c {}c) '.format(k,j))
    #     elif strA == 'strut_less':
    #         for i in range(len(listA)):
    #             k, j = listA[i][0], listA[i][1]
    #             strB += ('('+strA+ ' {} {}) '.format(k,j))
    #     return strB
                
    # # iterate given a known range and create lists of the form [0,1,2,3,4,5]
    # # although the one below is not using the addVars is kept because is less lines
    # def theIterator(self, anArray, start, stop, replaceWith):
    #     anArray = str(list(range(start, anArray + stop)))
    #     # cleanup an array from commas and brackets then replace with strings
    #     anArray = anArray.replace(',', replaceWith)
    #     anArray = anArray.replace('[', '')
    #     anArray = anArray.replace(']', '')
    #     return anArray
    
    # # deliver strings contating less/plus variables
    # def plusOrMimusN(self, maxOfCoods, Value, name):
        
    #     # iterate and create a list at a known range = maxOfCoods
    #     entryList = list(range(0, maxOfCoods))
    #     print('plus= ', entryList)
        
    #     # create a second list that holds the difference from the entryList based on the value
    #     # making sure that result is less than the list element's value + value
    #     plusList = [x+Value for x in entryList if x+Value <= maxOfCoods]
    #     print('plus2= ',plusList)
        
    #     # combine the two lists into one
    #     combList = [list(a) for a in zip(entryList, plusList)]
    #     print('combList= ', combList)
    #     # check is the the strut_less is called then revert the list of lists, hence, 1 2, 3 4 becomes 2 1, 4 3
    #     if name == 'strut_less':
    #         combList = [li[::-1] for li in combList]   # revert 
    #     return self.addVars(combList, name)
        
        