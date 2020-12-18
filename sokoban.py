# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:32:03 2020

@author: G. Mastorakis
"""


# Define Sokoban 

# Generate a demo problem for Sokoban

# location has x&y coordinates
# elements is always one as we have one player and the location of the player is the entry point without changing the coordinate
# rename entry point to starting point in GUI
# have two types of obstacles: hard and movable
# when setting starting point do not change the grid's origin

class sokoban():
    def __init__(self):
        self.locList = []
        self.goalList = []
        self.geometryList = []
        self.clist = []
        self.playerList = []
        self.stonesList = []
        
        self.xMax = 0
        self.zMax = 0
        

    def generatePDDLproblem(self, domain, problemName, location, stones, player, goal):
        print('sokoban')
        print('players= ', player)
        print('stones= ', stones)
        print('location ' , location)
        #player = [[1,1,1],[2,2,2]]
        # print("location is of type {} and has value of {}".format(type(location), location))
        with open('problem_'+problemName+'.pddl', 'w') as fp:
                fp.write("(define (problem " + problemName + ") (:domain " + domain + ")\n")
                fp.write("\t(:objects \n")
                fp.write("\t dir-down - direction\n\t dir-left - direction\n\t dir-right - direction \n\t dir-up - direction \n")
                fp.write(self.setVars(player, 'player') + " \n\n")
                #fp.write(self.theCleaner2(location, '') +"\n")
                fp.write(self.setGrid(location))
                fp.write(self.setVars(stones, 'stone') + "\n")
                fp.write("\t)\n")    
                fp.write("\t(:init\n")
                fp.write(self.setVars(goal, 'IS-GOAL pos-' )+"\n") # IS-GOAL
                #print(self.goalList)
                
               
                fp.write(self.setVars(self.subtract(self.locList, self.goalList),'IS-NONGOAL pos-')) 
                
               
                for num in self.MoveDirection(self.xMax, self.zMax, self.locList, self.goalList, self.playerList):
                    fp.write(f"\t {num}\n")
                    
                print(self.locList, ' geom : ', self.geometryList)
                fp.write(self.setVars(player, 'at player' )+"\n")
                fp.write(self.setVars(stones, 'at stone')) # goal list already removed from geometry coords - see previous subtract
                
                
                fp.write('\n' + self.setVars(self.createCleanList(self.locList, self.geometryList), 'clear pos'))
                
                fp.write("(= (total-cost) 0)\n)")
                fp.write("\n (:goal (and \n ")
                fp.write(self.setVars(self.goalList, 'at-goal' )+ '\n))')
                
                fp.write("\n\t(:metric minimize (total-cost)) \n)")

      # produce pos-1-1 - location

                
    def setGrid(self, file):
        output = ''
        
        # get the max in x, z then iterate 
        self.xMax = max(map(lambda x: x[0], file))
        self.zMax = max(map(lambda z: z[2], file))
        print('xmax= ' + str(self.xMax), 'zmax= ', str(self.zMax))
        for x in range(1, self.xMax):
            for z in range(1, self.zMax):
               output = output  + '\t pos-' + str(x) + '-' + str(z) + ' - location\n'
               self.locList.append([x,z])
        
     
        return str(output) # no need str here
    
  
    # this is using the subtract function
    def createCleanList(self, a, b):
         first_tuple_list = [tuple(lst) for lst in a]
         secnd_tuple_list = [tuple(lst) for lst in b]
         first_set = set(first_tuple_list)
         secnd_set = set(secnd_tuple_list)
         
         res = first_set & secnd_set
         out = first_set - res
         
         out = self.subtract(out, self.playerList)
         
         out = self.subtract(out, self.stonesList)
         
         #self.clist += self.goalList + list(out) # don't add the players in the clear list
         
         return list(out)
         
    # 
    def setVars(self, file, varName):
        anArray = ''
        if varName == 'stone':
            for i in range(len(file)):
                anArray = anArray + '\t ' + varName +'-0' + str(i+1) + ' - '+ varName +'\n'
        elif varName == 'IS-GOAL pos-':
            for i in range(len(file)):
                x, z = file[i][0], file[i][2]
                anArray = anArray + '\t (IS-GOAL pos-'  + str(x) + '-' + str(z)+')\n'
                self.goalList.append([x, z])
        elif varName == 'IS-NONGOAL pos-':
            for i in range(len(file)):
                x, z = file[i][0], file[i][1]
                anArray = anArray + '\t (IS-NONGOAL pos-'  + str(x) + '-' + str(z)+')\n'
        elif varName == 'at player':
            for i in range(len(file)):
                x, z = file[i][0], file[i][2]
                anArray = anArray + '\t (at player-0' + str(i+1)  +  ' pos-' + str(x) + '-' + str(z)+')\n'
                self.playerList.append([x, z])
        elif varName == 'player':
            for i in range(len(file)):
                anArray = anArray + '\t ' + varName +'-0' + str(i+1) + ' - '+ varName +'\n'
        elif varName =='at stone':
            print('sksksk = ', file)
            for i in range(len(file)):
                x, z = file[i][0], file[i][2]
                anArray = anArray + '\t (at stone'+'-0' + str(i+1) + ' pos-'  + str(x) + '-' + str(z)+')\n'
                self.stonesList.append([x, z])
        elif varName == 'clear pos':
            for i in range(len(file)):
                x, z = file[i][0], file[i][1]
                anArray = anArray + '\t (clear pos-'  + str(x) + '-' + str(z)+')\n'
        elif varName == 'at-goal':
            for i in range(len(file)):
                anArray = anArray + '\t (at-goal stone-0' + str(i+1) +')\n'
                
        return anArray
    
    
    
     
    
    def subtract(self, a, b):
        
        first_tuple_list = [tuple(lst) for lst in a]
        secnd_tuple_list = [tuple(lst) for lst in b]
        first_set = set(first_tuple_list)
        secnd_set = set(secnd_tuple_list)
        
        return list(first_set - secnd_set)
    
        
    def MoveDirection(self, dim1, dim2, clist, glist, plist):
               
        moveDirections = []
        
       
      
        for i in range(0, dim1):
            for j in range(0, dim2):
              #  print([i,j])
                for k in range(len(clist)):
                    for l in range(len(clist)):
                        if [i,j] == clist[k]:
                            if ([i,j-1] == clist[l]): # up
                                UP = str("(MOVE-DIR pos-" + str(i)+"-"+str(j) + " pos-" + str(i) + "-" + str(j-1) + " dir-up)")
                                moveDirections.append(UP)
                               
                            elif ([i,j+1] == clist[l]): # down
                              
                                DOWN = str("(MOVE-DIR pos-" + str(i)+"-"+str(j) + " pos-" + str(i) + "-" + str(j+1) + " dir-down)")
                                moveDirections.append(DOWN)
                               
                            elif ([i+1,j] == clist[l]): # right
                                
                                RIGHT = str("(MOVE-DIR pos-" + str(i)+"-"+str(j) + " pos-" + str(i+1) + "-" + str(j) + " dir-right)")
                                moveDirections.append(RIGHT)
                              
                            elif ([i-1,j] == clist[l]): # left
                                
                                LEFT = str("(MOVE-DIR pos-" + str(i)+"-"+str(j) + " pos-" + str(i-1) + "-" + str(j) + " dir-left)")
                                moveDirections.append(LEFT)
                                
        
        return moveDirections
    