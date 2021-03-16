"""
@authors G. Mastorakis, B. Lazaruk, J. Roberts
"""

from vtk import vtkPropAssembly, vtkPropPicker, vtkPropCollection, vtkCaptionActor2D
from vis import colours, opacities
import scanScene
import numpy as np

def set_axis(renwinRef, renderers, annotations, axisRef, axesActor, key):
    # called when the axis button is clicked in the UI or the keypress 'a'
    status = axisRef.isChecked()
    if (key == 'key'):
        if (status == True):
            renderers[annotations].RemoveActor(axesActor)
            axisRef.setChecked(False)
        else:
            renderers[annotations].AddActor(axesActor)
            axisRef.setChecked(True)
    if (key != 'key'):
        if (axisRef.isChecked()):
            renderers[annotations].AddActor(axesActor)
        else:
            renderers[annotations].RemoveActor(axesActor)
    renwinRef.Render()
    return

def set_grid(renwinRef, renderers, annotations, gridRef, gridActor, key):
    # called when the grid button is clicked in the UI or the keypress 'g'
    status = gridRef.isChecked()
    if (key == 'key'):
        if (status == True):
            renderers[annotations].RemoveActor(gridActor)
            gridRef.setChecked(False)
        else:
            renderers[annotations].AddActor(gridActor)
            gridRef.setChecked(True)
    if (key != 'key'):
        if (gridRef.isChecked()):
            renderers[annotations].AddActor(gridActor)
        else:
            renderers[annotations].RemoveActor(gridActor)
    renwinRef.Render()
    return

def toggleCaptionsold(renwinRef, renderers, blocks, showCoordsRef, progressBarRef, key):
    # Activates on keypress "c"
    # If the key is used, switch the status of the checkbox
    if (key == 'key'):
        if (showCoordsRef.isChecked() == True):
            showCoordsRef.setChecked(False)
        else:
            showCoordsRef.setChecked(True)

    progressBarRef.setProperty("value", 0)
    iteration = 0

    wallProps = scanScene.get_wall_props(renderers, blocks)
    numberProps = len(wallProps)
    for currentProp in wallProps:
        tx, ty, tz = int(currentProp.GetBounds()[1]), int(currentProp.GetBounds()[3]), int(currentProp.GetBounds()[5])
        # Now, test the world coordinate immediately "above" this prop by incrementing the y axis and performing a pick at that location.
        # If the picker returns a 1 then there is a prop at the modified location.
        # If there is a prop there then this prop is not the "highest" on the y-axis and therefore no caption is needed.
        modty = ty + 1
        picker = vtkPropPicker()
        propAbove = picker.Pick3DPoint((tx,modty,tz), renderers[blocks])
        if propAbove == 0:
            # This prop is the "highest" on the y-axis
            captionPossible = True
        else:
            # There is a prop "above" this prop on the y-axis
            captionPossible = False

        numberOfActors = currentProp.GetNumberOfPaths()

        # setup a vtkPropAssembly to store the assembly of parts that make up the current prop, and populate it
        actorCollection = vtkPropAssembly()
        actorCollection = currentProp.GetParts()

        # and initiate traversal over the collection of parts/actors
        actorCollection.InitTraversal()
        for actor in range(numberOfActors):
            # now iterate over each actor
            # move to the next actor in the collection
            currentActor = actorCollection.GetNextProp()

            # check if this actor is a caption type, and if so then set its opacity based on the checkbox and "height"
            # method returns a 1 if the type of the actor matches the argument, otherwise returns a 0
            typeBool = currentActor.IsTypeOf("vtkCaptionActor2D")
            if typeBool == 1:
                # this actor is a caption type, so if captionPossible is True then set the current opacity of the text
                # and the leader to match the status of the checkbox
                if captionPossible == True and showCoordsRef.isChecked() == True:
                    currentActor.GetCaptionTextProperty().SetOpacity(1)
                    currentActor.LeaderOn()
                else:
                    # captionPossible is False so there is a prop "above" this prop and the caption should be suppressed
                    # Or the master switch for the captions is off
                    # Force the caption opacity to 0
                    currentActor.GetCaptionTextProperty().SetOpacity(0)
                    currentActor.LeaderOff()
        # Update the progress bar
        iteration += 1
        percentComplete = int((iteration / numberProps) * 100)
        progressBarRef.setProperty("value", percentComplete)
    renwinRef.Render()
    return

def toggleCaptions(renwinRef, renderers, blocks, showCoordsRef, progressBarRef, key):
    # Activates on keypress "c"
    # If the key is used, switch the status of the checkbox
    if (key == 'key'):
        if (showCoordsRef.isChecked() == True):
            showCoordsRef.setChecked(False)
        else:
            showCoordsRef.setChecked(True)

    progressBarRef.setProperty("value", 0)
    iteration = 0

    if showCoordsRef.isChecked() == True:
        wallCoordinates, _, _ = scanScene.get_wall_positions(renderers, blocks)
        maxLength, maxWidth, _, _ = scanScene.get_scene_bounds(renderers, blocks)

        for x in range(maxLength + 1):
            for z in range(maxWidth + 1):
                subList = [point for point in wallCoordinates if point[0] == x and point[2] == z]
                sortedSubList = sorted(subList, key=lambda k: [k[1]], reverse=True)
                if len(sortedSubList) > 0:
                    picker = vtkPropPicker()
                    propPicked = picker.Pick3DPoint(sortedSubList[0], renderers[blocks])
                    targetProp = picker.GetViewProp()
                    caption = vtkCaptionActor2D()
                    caption.SetCaption("(" + str(x) + ", " + str(z) + ")")
                    caption.SetWidth(0.15)
                    caption.SetHeight(0.02)
                    caption.GetProperty().SetColor(colours['captionColour'])
                    caption.SetAttachmentPoint(x, sortedSubList[0][1], z)
                    caption.BorderOff()
                    targetProp.AddPart(caption)
    else:
        # Remove all captions
        wallProps = scanScene.get_wall_props(renderers, blocks)
        numberProps = len(wallProps)
        for currentProp in wallProps:
            numberOfActors = currentProp.GetNumberOfPaths()

            # setup a vtkPropAssembly to store the assembly of parts that make up the current prop, and populate it
            actorCollection = vtkPropAssembly()
            actorCollection = currentProp.GetParts()

            # and initiate traversal over the collection of parts/actors
            actorCollection.InitTraversal()
            for actor in range(numberOfActors):
                # now iterate over each actor
                # move to the next actor in the collection
                currentActor = actorCollection.GetNextProp()
                # check if this actor is a caption type, and if so then set its opacity based on the checkbox and "height"
                # method returns a 1 if the type of the actor matches the argument, otherwise returns a 0
                typeBool = currentActor.IsTypeOf("vtkCaptionActor2D")
                if typeBool == 1:
                    # this actor is a caption type, so remove it
                    currentProp.RemovePart(currentActor)

    renwinRef.Render()
    return



def toggleWallTransparency(renwinRef, renderers, blocks, transparentRef, progressBarRef, key):
    # Currently doesn't respond to keypreses
    # If the key is used, switch the status of the checkbox
    if (key == 'key'):
        if (transparentRef.isChecked() == True):
            transparentRef.setChecked(False)
        else:
            transparentRef.setChecked(True)

    progressBarRef.setProperty("value", 0)
    iteration = 0

    if transparentRef.isChecked() == True:
        opacity = opacities['transparent']
    else:
        opacity = opacities['opaque']

    # Get a list of the wall actors in the scene
    wallActors = scanScene.get_wall_actors(renderers, blocks)
    numberActors = len(wallActors)
    for currentActor in wallActors:
        # check each of the actors and if it is currently an inert wall then set the opacity to match the current setting
        targetActorColours = currentActor.GetProperty().GetColor()
        if (targetActorColours == colours['intWallInert']) or \
            (targetActorColours == colours['extWallInert']):
                currentActor.GetProperty().SetOpacity(opacity)
        # Update the progress bar
        iteration += 1
        percentComplete = int((iteration / numberActors) * 100)
        progressBarRef.setProperty("value", percentComplete)

    renwinRef.Render()
    return
