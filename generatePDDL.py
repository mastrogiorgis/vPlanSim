"""
@authors G. Mastorakis, B. Lazaruk, J. Roberts
"""

import os
import scanScene
#import connect_r as cr
import sokoban as sb
import derived_drone as dr

def writefile(renderers, blocks, dName, problemText, elementsNo):
    # Open the file handle, which overwrites any previously existing data and in the case that the user generates PDDL without any goals defined, clears the file
    pddlFileHandle = open('pddl.txt', 'w')
    # Get python lists of wall actor positions, external wall positions, and ALL other cube actor positions
    wall_coordinates, extWall_coordinates, intWall_coordinates = scanScene.get_wall_positions(renderers, blocks)
    # Get list of unique goals
    goal_coordinates = scanScene.get_goal_positions(renderers, blocks)
    # Get list of unique entry points
    entry_coordinates = scanScene.get_entry_positions(renderers, blocks)
    # Get list of unique element locations
    element_coordinates = scanScene.get_element_positions(renderers, blocks)
    

    # External walls are all the cubes which are flagged as external walls.
    # Internal walls are all cubes which are not external walls, which is the interior walls and obstacles
    # Goals, entries, and elements are just those positions as defined by the colour of the object they are attached to

    # Right now the internal walls list is everything that is not explicitly an external wall. This includes ALL
    # wall actors that are also entries or goals.

    # Remove anything from the internal list which is also in the external list, goal list, or entry list.
    # First, need to create temporary versions of the goals and entries lists, without the angle parameter
    tempGoal_coordinates = []
    tempEntry_coordinates = []
    for tempGoal in goal_coordinates:
        tempGoal_coordinates.append(tempGoal[:-1])
    for tempEntry in entry_coordinates:
        tempEntry_coordinates.append(tempEntry[:-1])

    # And now remove anything from the internal walls list which is also in external walls, goals, or entries
    # Have to parse backwards as we're removing elements from the array itself (see, I was paying attention in class!)
    for internal in intWall_coordinates[::-1]:
        if internal in extWall_coordinates:
            intWall_coordinates.remove(internal)
        if internal in tempGoal_coordinates:
            intWall_coordinates.remove(internal)
        if internal in tempEntry_coordinates:
            intWall_coordinates.remove(internal)

    # Only build the PDDL if there are walls, an entry point, and at least one goal point
    if (len(wall_coordinates) > 0) and (len(goal_coordinates) > 0) and (len(entry_coordinates) > 0) and (len(element_coordinates) > 0 or (elementsNo > 0)):
        # use these lists to store the prepared PDDL code
        goalsFullList = []
        wallsFullList = []
        entriesFullList = []
        elementsFullList = []

        pddlFileHandle.write("Walls: [")
        for line in wall_coordinates:
            pddlFileHandle.write(str(line) + ",")
            wallsFullList.append(line)
        pddlFileHandle.write("]")

        pddlFileHandle.write("\nGoals: [")

        for line in goal_coordinates:
            pddlFileHandle.write(str(line) + ",")
            goalsFullList.append(line)
        pddlFileHandle.write("]")

        pddlFileHandle.write("\nEntries: [")
        for line in entry_coordinates:
            pddlFileHandle.write(str(line) + ",")
            entriesFullList.append(line)
        pddlFileHandle.write("]")

        pddlFileHandle.write("\nElements: [")
        for line in element_coordinates:
            pddlFileHandle.write(str(line) + ",")
            elementsFullList.append(line)
        pddlFileHandle.write("]")
        
        

        # # get the domain name from the combobox
        # dName = str(self.domainName.currentText())

        # if item from combobox is Sokoban
        if dName == 'Sokoban':
            soko = sb.sokoban()
            # call sokoban function to generate PDDL problem file
            soko.generatePDDLproblem('p01-domain', problemText, wallsFullList, elementsFullList, entriesFullList, goalsFullList)
        elif dName == 'Drone':
            dron = dr.drone()
            dron.generatePDDLproblem('derived_drone', problemText, wallsFullList, elementsNo, entriesFullList, goalsFullList)
    else:
        # At least one of the lists of data is empty, which is not supported. So write an error to the exported file.
        pddlFileHandle.write("Please ensure the scene has some walls, at least one goal point, one entry point, and at least one element.")
    pddlFileHandle.close()

def preview(renderers, blocks, dName, problemText, elementsNo):
    # Call the generate PDDL to get the data ready
    writefile(renderers, blocks, dName, problemText, elementsNo)
    # Then open the file for the user
    os.startfile('problem_' + problemText + '.pddl')