"""
@authors G. Mastorakis, B. Lazaruk, J. Roberts
"""

from vis import cube_from_source
import floormethods
import annotate
import scanScene

def setWalls(renwinRef, renderers, blocks, objLengthX, objHeightY, objWidthZ, progressBarRef, showCoordsRef, floorRef, transparencyRef):
    # Called when the set button is clicked in the outside walls UI
    # This is basically "draw a rectangle, measured from 0,0,0 to the length, width, height specified
    # Iterate over the all the z over all the y, and those over all the x
    # Only build an actor when the x or z is 0 or at the maximum range
    # So as to build a hollow object representing the exterior walls only, and not a monolithic block

    showCoordsBool = showCoordsRef.isChecked()
    wallsTransparentBool = transparencyRef.isChecked()
    # Prep undoCollection to be returned, and individual undoSet for activities in this function
    undoCollection = []
    undoWalls = ['removeactor', blocks]

    progressBarRef.setProperty("value", 0)
    iteration = 0
    # Reduce number of cubes by 4 so the corners are not counted twice
    numberPotentialCubes = max((((objLengthX + objWidthZ - 4) * 2) * objHeightY), 1)
    for x in range(objLengthX):
        for z in range(objWidthZ):
            for y in range(objHeightY):
                if x == 0 or x == (objLengthX - 1) or z == 0 or z == (objWidthZ - 1):
                    # Only needs to build a cube on the min or max of the x (length) or z (width) axes
                    # Send the x, y, z coordinates to the helper function, which returns a vtkPropAssembly
                    # consisting of a cube and a caption
                    actorcube = cube_from_source(x, y, z, showCoordsBool, 'extWallInert', wallsTransparentBool)
                    # Add the new prop to the blocks renderer
                    renderers[blocks].AddActor(actorcube)
                    # Add the new prop to the undoSet as well
                    # undoWalls.append(actorcube)
                    # Update the progress bar
                    iteration += 1
                    percentComplete = int((iteration / (numberPotentialCubes + 1)) * 100)
                    progressBarRef.setProperty("value", percentComplete)

    # If the coordinate captions are visible then they need to be reset as the lower blocks with suppressed captions will now be on "top"
    if showCoordsBool == True:
        annotate.toggleCaptions(renwinRef, renderers, blocks, showCoordsRef, progressBarRef, "")

    # Call setFloor which will check the status of the toggle button and add the floor if requested
    undoFloors = floormethods.setFloor(renwinRef, renderers, blocks, floorRef, progressBarRef, "")

    # Build the undoCollection
    undoCollection.append(undoWalls)
    undoCollection.append(undoFloors)

    return undoCollection

def setInWalls_2X(renwinRef, renderers, blocks, objPosX, objWidthZ, objHeightY, progressBarRef, showCoordsRef, transparencyRef):
    showCoordsBool = showCoordsRef.isChecked()
    wallsTransparentBool = transparencyRef.isChecked()
    # Prep undoSet
    undoSet = ['removeactor', blocks]
    progressBarRef.setProperty("value", 0)
    iteration = 0
    numberPotentialCubes = objPosX * objHeightY
    for x in range(objPosX):
            for y in range(objHeightY):
                actorcube = cube_from_source(x, y, objWidthZ, showCoordsBool, 'intWallInert', wallsTransparentBool)
                renderers[blocks].AddActor(actorcube)
                # Add the new prop to the undoSet as well
                undoSet.append(actorcube)
                # Update the progress bar
                iteration += 1
                percentComplete = int((iteration / numberPotentialCubes) * 100)
                progressBarRef.setProperty("value", percentComplete)

    # If the coordinate captions are visible then they need to be reset as the lower blocks with suppressed captions will now be on "top"
    if showCoordsBool == True:
        # self.toggleCaptions(self)
        annotate.toggleCaptions(renwinRef, renderers, blocks, showCoordsRef, progressBarRef, "")

    return undoSet

def setInWalls_2Z(renwinRef, renderers, blocks, objPosX, objWidthZ, objHeightY, progressBarRef, showCoordsRef, transparencyRef):
    showCoordsBool = showCoordsRef.isChecked()
    wallsTransparentBool = transparencyRef.isChecked()
    # Prep undoSet
    undoSet = ['removeactor', blocks]
    progressBarRef.setProperty("value", 0)
    iteration = 0
    numberPotentialCubes = objWidthZ * objHeightY
    for z in range(objWidthZ):
            for y in range(objHeightY):
                actorcube = cube_from_source(objPosX, y, z, showCoordsBool, 'intWallInert', wallsTransparentBool)
                renderers[blocks].AddActor(actorcube)
                # Add the new prop to the undoSet as well
                undoSet.append(actorcube)
                # Update the progress bar
                iteration += 1
                percentComplete = int((iteration / numberPotentialCubes) * 100)
                progressBarRef.setProperty("value", percentComplete)

    # If the coordinate captions are visible then they need to be reset as the lower blocks with suppressed captions will now be on "top"
    if showCoordsBool == True:
        # self.toggleCaptions(self)
        annotate.toggleCaptions(renwinRef, renderers, blocks, showCoordsRef, progressBarRef, "")

    return undoSet

def truncateWalls(renwinRef, renderers, blocks, roomYValue, progressBarRef, showCoordsRef):
    heightThreshold = max(roomYValue, 1) - 1
    showCoordsBool = showCoordsRef.isChecked()

    # Prep undoSet
    undoSet = ['addactor', blocks]
    # Get the list of wall prop objects
    wallProps = scanScene.get_wall_props(renderers, blocks)
    for currentProp in wallProps:
        tx, ty, tz = int(currentProp.GetBounds()[1]), int(currentProp.GetBounds()[3]), int(currentProp.GetBounds()[5])
        # If the ty value exceeds the threshold, remove the prop
        if ty > heightThreshold:
            # This prop is too high on the y-axis
            # Add it to the undoSet
            undoSet.append(currentProp)
            # Remove it from the renderer
            renderers[blocks].RemoveActor(currentProp)

    # If the coordinate captions are visible then they need to be reset as the lower blocks with suppressed captions will now be on "top"
    if showCoordsBool == True:
        annotate.toggleCaptions(renwinRef, renderers, blocks, showCoordsRef, progressBarRef, "")

    return undoSet