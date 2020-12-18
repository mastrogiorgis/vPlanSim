"""
@authors G. Mastorakis, B. Lazaruk, J. Roberts
"""

import vis as graphics
import scanScene

def setFloor(renwinRef, renderers, blocks, floorRef, progressBarRef, key):
    # called when the floor button is clicked in the UI or the keypress 'f'

    status = floorRef.isChecked()
    if (key == 'key'):
        if (status == True):
            undoSet = removeFloor(renderers, blocks)
            floorRef.setChecked(False)
        else:
            undoSet = addFloor(renderers, blocks, progressBarRef)
            floorRef.setChecked(True)
    if (key != 'key'):
        if (floorRef.isChecked()):
            undoSet = addFloor(renderers, blocks, progressBarRef)
        else:
            undoSet = removeFloor(renderers, blocks)
    renwinRef.Render()
    return undoSet

def removeFloor(renderers, blocks):
    # Prep undoSet
    undoSet = ['addactor', blocks]
    # Get the floor actors from the scene
    floorActors = scanScene.get_floor_actors(renderers, blocks)
    # Iterate over the actors
    for currentProp in floorActors:
        # Add this new panel to the undoset
        undoSet.append(currentProp)
        # And remove it from the renderer
        renderers[blocks].RemoveActor(currentProp)
    return undoSet

def addFloor(renderers, blocks, progressBarRef):
    # Add floor needs to be cleaned up after it's decided about how many levels of floor will be available.
    # Prep undoSet
    undoSet = ['removeactor', blocks]
    # Get the scene bounds
    maxLength, maxWidth, minLength, minWidth = scanScene.get_scene_bounds(renderers, blocks)
    # And calculate the number of possible floor panels from the scene bounds
    numberPotentialPanels = ((maxLength - minLength) * (maxWidth - minWidth))

    # And now we have the minimum and maximum X and Z values for the given level, and the number of panels that will be added to the floor
    # Setup the progress bar
    progressBarRef.setProperty("value", 0)
    iteration = 0
    # Finally, add the floor objects within the bounds of the walls
    for i in range(minLength, maxLength + 1):
        for j in range(minWidth, maxWidth + 1):
            # Offset the height of the floor panel by 0.5, to drop the floor block to a position below the wall blocks
            actorpanel = graphics.floor_panel([i, -0.5, j], 1, 1)
            # Add the floor panel to the renderer
            renderers[blocks].AddActor(actorpanel)
            # Add this new panel to the undoset
            undoSet.append(actorpanel)
            # Update the progress bar
            iteration += 1
            percentComplete = int((iteration / numberPotentialPanels) * 100)
            progressBarRef.setProperty("value", percentComplete)

    return undoSet