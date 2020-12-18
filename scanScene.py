"""
@authors G. Mastorakis, B. Lazaruk, J. Roberts
"""

from vis import colours
from vtk import vtkPropCollection, vtkPropAssembly
import numpy as np
import math

def get_wall_props(renderers, blocks):
    # Returns a list of the vtkPropAssembly props which are wall and obstacle objects with embedded captions
    # Setup the list to collect the props
    propsList = []
    # A vtkPropCollection, populate it with the props from the blocks renderer
    propCollection = vtkPropCollection()
    propCollection = renderers[blocks].GetViewProps()
    # Get the number of props so we know how many items to iterate over
    numberProps = propCollection.GetNumberOfItems()
    # Initiate traversal over the collection
    propCollection.InitTraversal()
    # Now iterate over each of the props
    for prop in range(numberProps):
        # Move to the next prop in the collection and get the number of actors in that prop
        currentProp = propCollection.GetNextProp()
        # We're just interested in wall objects, not floor objects
        # So only scan this prop further if it is a prop and not an actor
        typeBool = currentProp.IsTypeOf("vtkPropAssembly")
        if typeBool == 1:
            # This is a wall object prop
            propsList.append(currentProp)
    return propsList

def get_scene_bounds(renderers, blocks):
    # Returns the largest and smallest (x,z) position for all wall objects in the scene
    # Initialize the maximums and minimums for comparison
    maxLength = 0
    maxWidth = 0
    minLength = 999
    minWidth = 999
    # Get the list of wall actors
    wallActors = get_wall_actors(renderers, blocks)
    # And iterate over the list, checking the objects position
    for currentActor in wallActors:
        # Compare its x and z coordinates to the known maximum and minimum of the objects. Update the minimum and maximum as necessary.
        if maxLength < currentActor.GetBounds()[1]:
            maxLength = currentActor.GetBounds()[1]
        if maxWidth < currentActor.GetBounds()[5]:
            maxWidth = currentActor.GetBounds()[5]
        if minLength > currentActor.GetBounds()[1]:
            minLength = currentActor.GetBounds()[1]
        if minWidth > currentActor.GetBounds()[5]:
            minWidth = currentActor.GetBounds()[5]
    # Now convert the minimums and maximums to integers
    maxLength = int(maxLength)
    maxWidth = int(maxWidth)
    minLength = int(minLength)
    minWidth = int(minWidth)

    return maxLength, maxWidth, minLength, minWidth

def get_wall_actors(renderers, blocks):
    # Returns a list of just the actor components from the wall cube props
    # Setup the list to collect the actors
    actorsList = []
    # A vtkPropCollection, populate it with the props from the blocks renderer
    propCollection = vtkPropCollection()
    propCollection = renderers[blocks].GetViewProps()
    # Get the number of props so we know how many items to iterate over
    numberProps = propCollection.GetNumberOfItems()
    # Initiate traversal over the collection
    propCollection.InitTraversal()
    # Now iterate over each of the props
    for prop in range(numberProps):
        # Move to the next prop in the collection and get the number of actors in that prop
        currentProp = propCollection.GetNextProp()
        # We're just interested in wall objects, not floor objects
        # So only scan this prop further if it is a prop and not an actor
        typeBool = currentProp.IsTypeOf("vtkPropAssembly")
        if typeBool == 1:
            # The prop doesn't list any positional attributes so we're going to need to loop over the component actors to find the cube actor which does have positional attributes
            # Get the number of actors in this prop so we know how many iterations to make
            numberOfActors = currentProp.GetNumberOfPaths()
            # Setup a vtkPropAssembly to store the assembly of parts that make up the current prop, and populate it
            actorCollection = vtkPropAssembly()
            actorCollection = currentProp.GetParts()
            # and initiate traversal over the collection of parts/actors
            actorCollection.InitTraversal()
            for actor in range(numberOfActors):
                # Now iterate over each actor.
                # Move to the next actor in the collection.
                currentActor = actorCollection.GetNextProp()
                # Check if the actor is an OpenGL type, which is used for the wall and floor objects, as opposed to a CaptionActor type which is the component used for the captioning
                # method returns a 1 if the type of the actor matches the argument, otherwise returns a 0
                typeBool = currentActor.IsTypeOf("vtkOpenGLActor")
                if typeBool == 1:
                    # This actor is a wall or floor actor
                    # check the height of the actor ... if it's less than 1 then this actor is floor
                    actorHeight = currentActor.GetBounds()[3] - currentActor.GetBounds()[2]
                    if actorHeight >= 1:
                        # This is a wall actor
                        actorsList.append(currentActor)
    return actorsList

def get_floor_actors(renderers, blocks):
    # Returns a list of just the floor panel actors
    # Setup the list to be returned
    actorsList = []
    # Setup a vtkPropCollection, get populate it with the props from the blocks renderer
    propCollection = vtkPropCollection()
    propCollection = renderers[blocks].GetViewProps()
    # Get the number of props so we know how many items to iterate over
    numberProps = propCollection.GetNumberOfItems()
    # Initiate traversal over the collection
    propCollection.InitTraversal()
    # now iterate over each of the props
    for prop in range(numberProps):
        # Move to the next prop in the collection and get the number of actors in that prop
        currentProp = propCollection.GetNextProp()
        # Check if this prop is an OpenGLActor
        typeBool = currentProp.IsTypeOf("vtkOpenGLActor")
        if typeBool == 1:
            # This is an actor, which means its part of the floor.
            actorsList.append(currentProp)
    return actorsList

def get_wall_positions(renderers, blocks):
    # Returns all walls, which is the positions of all cube actors, external walls which is the position of all
    # cubes of colour = 'extWallInert', and internal walls which is cube actors that are not external walls.
    # This will include ALL goals and entry points, even if they are on external walls.

    # Set up lists, some need to exist so they can be returned even if empty, some so they can be appended to
    wall_coordinates_list = []
    extWall_coordinates_list = []
    intWall_coordinates_list = []
    wall_coordinates_unique = []
    extWall_coordinates_unique = []
    intWall_coordinates_unique = []
    final_wall_list = []
    final_extWall_list = []
    final_intWall_list = []

    wallActors = get_wall_actors(renderers, blocks)
    for currentActor in wallActors:
        tx, ty, tz = math.ceil(currentActor.GetCenter()[0]), math.ceil(currentActor.GetCenter()[1]), math.ceil(
            currentActor.GetCenter()[2])
        wall_coordinates_list.append([tx, ty, tz])
        currentActorColour = currentActor.GetProperty().GetColor()
        if ((currentActorColour == colours['extWallInert']) or (currentActorColour == colours['extWallGoal']) or (
                currentActorColour == colours['extWallEntry'])):
            extWall_coordinates_list.append([tx, ty, tz])
        else:
            intWall_coordinates_list.append([tx, ty, tz])

    # Move the lists to numpy and export the unique coordinate
    # Also make sure that the lists have items in them first.
    if (len(wall_coordinates_list) > 0):
        wall_coordinates_array = np.array(wall_coordinates_list)
        wall_coordinates_unique = np.unique(wall_coordinates_array, axis=0)
    if (len(extWall_coordinates_list) > 0):
        extWall_coordinates_array = np.array(extWall_coordinates_list)
        extWall_coordinates_unique = np.unique(extWall_coordinates_array, axis=0)
    if (len(intWall_coordinates_list) > 0):
        intWall_coordinates_array = np.array(intWall_coordinates_list)
        intWall_coordinates_unique = np.unique(intWall_coordinates_array, axis=0)
    # Export the arrays back to lists, so long as the arrays are not empty
    # If they are still lists then there was never any data to convert to numpy, so if they are lists they are empty
    if (len(wall_coordinates_unique) > 0):
        final_wall_list = wall_coordinates_unique.tolist()
    if (len(extWall_coordinates_unique) > 0):
        final_extWall_list = extWall_coordinates_unique.tolist()
    if (len(intWall_coordinates_unique) > 0):
        final_intWall_list = intWall_coordinates_unique.tolist()
    return final_wall_list, final_extWall_list, final_intWall_list

def get_goal_positions(renderers, blocks):
    # Returns a list of the goal positions in the scene
    # Prep the list which will hold the goal coordinates
    goal_coordinates_list = []
    goal_coordinates_unique = []
    final_goals_list = []
    # Get the wall actors and check them for goals
    wallActors = get_wall_actors(renderers, blocks)
    for currentActor in wallActors:
        currentActorColours = currentActor.GetProperty().GetColor()
        if ((currentActorColours == colours['intWallGoal']) or (currentActorColours == colours['extWallGoal'])):
            # This wall actor is a goal, so add it to the list of goals
            tx, ty, tz = int(currentActor.GetBounds()[1]), int(currentActor.GetBounds()[3]), int(currentActor.GetBounds()[5])
            # Extract the angle from the edgecolor
            ax, ay, az = int(currentActor.GetProperty().GetEdgeColor()[0]), int(currentActor.GetProperty().GetEdgeColor()[1]), int(currentActor.GetProperty().GetEdgeColor()[2])
            goalAngle = (ax * 100) + (ay * 10) + (az)
            goal_position = [tx, ty, tz, goalAngle]
            goal_coordinates_list.append(goal_position)

    # Get the floor actors and check them for goals
    floorActors = get_floor_actors(renderers, blocks)
    for currentProp in floorActors:
        currentPropColour = currentProp.GetProperty().GetColor()
        if currentPropColour == colours['floorGoal']:
            # This floor panel is a goal, so add it to the list of goals
            tx, ty, tz = int(currentProp.GetBounds()[1]), int(currentProp.GetBounds()[3]), int(currentProp.GetBounds()[5])
            # Extract the angle from the edgecolor
            ax, ay, az = int(currentProp.GetProperty().GetEdgeColor()[0]), int(
                currentProp.GetProperty().GetEdgeColor()[1]), int(currentProp.GetProperty().GetEdgeColor()[2])
            goalAngle = (ax * 100) + (ay * 10) + (az)
            goal_position = [tx, ty, tz, goalAngle]
            goal_coordinates_list.append(goal_position)

    if len(goal_coordinates_list) > 0:
        # Clean the goals list to ensure there are no duplicates
        # Define the numpy array to hold the goals
        goal_coordinates_array = np.array(goal_coordinates_list)
        # Remove all but unique entries in the array
        goal_coordinates_unique = np.unique(goal_coordinates_array, axis=0)

    # If the array has data then export it back to a list
    if (len(goal_coordinates_unique) > 0):
        final_goals_list = goal_coordinates_unique.tolist()
    return final_goals_list
    # return goal_coordinates_unique

def get_entry_positions(renderers, blocks):
    # Returns a list of the entry positions in the scene
    # Prep the list which will hold the goal coordinates
    entry_coordinates_list = []
    entry_coordinates_unique = []
    final_entry_list = []
    # Get the wall actors and check them for entries
    wallActors = get_wall_actors(renderers, blocks)
    for currentActor in wallActors:
        currentActorColours = currentActor.GetProperty().GetColor()
        if ((currentActorColours == colours['intWallEntry']) or (currentActorColours == colours['extWallEntry'])):
            # This wall actor is an entry, so add it to the list of entries
            tx, ty, tz = int(currentActor.GetBounds()[1]), int(currentActor.GetBounds()[3]), int(currentActor.GetBounds()[5])
            # Extract the angle from the edgecolor
            ax, ay, az = int(currentActor.GetProperty().GetEdgeColor()[0]), int(currentActor.GetProperty().GetEdgeColor()[1]), int(currentActor.GetProperty().GetEdgeColor()[2])
            entryAngle = (ax * 100) + (ay * 10) + (az)
            entry_position = [tx, ty, tz, entryAngle]
            entry_coordinates_list.append(entry_position)

    # Get the floor actors and check them for goals
    floorActors = get_floor_actors(renderers, blocks)
    for currentProp in floorActors:
        currentPropColour = currentProp.GetProperty().GetColor()
        if currentPropColour == colours['floorEntry']:
            # This floor panel is an entry, so add it to the list of entries
            tx, ty, tz = int(currentProp.GetBounds()[1]), int(currentProp.GetBounds()[3]), int(currentProp.GetBounds()[5])
            # Extract the angle from the edgecolor
            ax, ay, az = int(currentProp.GetProperty().GetEdgeColor()[0]), int(currentProp.GetProperty().GetEdgeColor()[1]), int(currentProp.GetProperty().GetEdgeColor()[2])
            entryAngle = (ax * 100) + (ay * 10) + (az)
            entry_position = [tx, ty, tz, entryAngle]
            entry_coordinates_list.append(entry_position)

    # Test the entry list to ensure it is not empty before going to remove duplicates
    if len(entry_coordinates_list) > 0:
        # Clean the entry list to ensure there are no duplicates
        # Define the numpy array to hold the entries
        entry_coordinates_array = np.array(entry_coordinates_list)
        # Remove all but unique entries in the array
        entry_coordinates_unique = np.unique(entry_coordinates_array, axis=0)
    # If the array has data then export it back to a list
    if (len(entry_coordinates_unique) > 0):
        final_entry_list = entry_coordinates_unique.tolist()
    return final_entry_list

def get_element_positions(renderers, blocks):
    # Returns a list of the element positions in the scene
    # Prep the list which will hold the element coordinates
    element_coordinates_list = []
    element_coordinates_unique = []
    final_element_list = []

    # Get the floor actors and check them for elements
    floorActors = get_floor_actors(renderers, blocks)
    for currentProp in floorActors:
        currentPropColour = currentProp.GetProperty().GetColor()
        if currentPropColour == colours['floorElement']:
            # This floor panel is an entry, so add it to the list of entries
            tx, ty, tz = int(currentProp.GetBounds()[1]), int(currentProp.GetBounds()[3]), int(currentProp.GetBounds()[5])
            # Extract the angle from the edgecolor
            ax, ay, az = int(currentProp.GetProperty().GetEdgeColor()[0]), int(currentProp.GetProperty().GetEdgeColor()[1]), int(currentProp.GetProperty().GetEdgeColor()[2])
            elementAngle = (ax * 100) + (ay * 10) + (az)
            element_position = [tx, ty, tz, elementAngle]
            element_coordinates_list.append(element_position)

    # Test the element list to ensure it is not empty before going to remove duplicates
    if len(element_coordinates_list) > 0:
        # Clean the element list to ensure there are no duplicates
        # Define the numpy array to hold the elements
        element_coordinates_array = np.array(element_coordinates_list)
        # Remove all but unique elements in the array
        element_coordinates_unique = np.unique(element_coordinates_array, axis=0)
    # If the array has data then export it back to a list
    if (len(element_coordinates_unique) > 0):
        final_element_list = element_coordinates_unique.tolist()
    # And return the element list
    return final_element_list
