# vPlanSim
An Open Source Graphical Interface for the Visualisation and Simulation of AI Systems

## Requirements
Python3.7 +

VTK8.2 +

PyQt5 +


## Features of vPlanSim


The user defines the 3D geometry of the scene by adjusting the external and internal walls.

<img src="https://user-images.githubusercontent.com/23278410/110217077-14985600-7eaa-11eb-89f5-fbf00ac46937.png" width=400>

The tool offers several viewing angles and viewing helper functions such as the axis and origin of the 3D visual space, a continuous grid annotating the ground, the coordinates of the walls and the floor within the walls.

<img src="https://user-images.githubusercontent.com/23278410/110217184-a99b4f00-7eaa-11eb-994a-a39f50cb7b33.png" width=400>

The user can delete the entire scene or specific blocks from the walls and can also add obstacles on the floor. Also, the geometry can be adjusted using the following menu to undo/redo wall creation, obstacles insertion or block deletion.

<img src="https://user-images.githubusercontent.com/23278410/110217307-32b28600-7eab-11eb-9edd-d8098861fcdf.png" width=400>

The planning menu holds the generation of PDDL based on a particular domain and using the above geometry. The user can select the coordinates of goals, entries and elements, name the problem, then generate and preview the PDDL problem file.

<img src="https://user-images.githubusercontent.com/23278410/110217433-f3386980-7eab-11eb-858a-c1c5457465ea.png" width=400>

Finally, the user can visually simulate step-by-step the plan (after solving the PDDL problem).

<img src="https://user-images.githubusercontent.com/23278410/110217536-69d56700-7eac-11eb-96b6-da1d64e7174c.png" width=400>

<h1>Guide for new domains</h1>

Users can create their own generated PDDL problems by modifying the two given examples (sokoban.py and derived_drone.py). The generatePDDLproblem should be modified to reflect the new domain.
<img src="https://user-images.githubusercontent.com/23278410/110531814-f2a20c00-8113-11eb-8267-3e689915e174.png" width=400>

## Examples

<b>Sokoban domain</b>

Using domain found in https://github.com/AI-Planning/classical-domains/tree/master/classical/sokoban-opt08-strips

Required files to run the demo can be found under domain folder

<img src="https://user-images.githubusercontent.com/23278410/110846255-7e966e00-82a3-11eb-91a4-d09574753024.gif" width=400>

<b>Drone domain</b>

Using a bespoke drone domain

Required files to run the demo can be found under domain folder

<img src="https://user-images.githubusercontent.com/23278410/110845863-029c2600-82a3-11eb-99e0-cad0c7c4f475.gif" width=400>


## Citation
<hl>
Please cite our work if you use vPlanSim
 
 
```bib
@inproceedings{f285037a2054446b8435ef7e4b48c9df,
title = "vPlanSim: An Open Source Graphical Interface for the Visualisation and Simulation of AI Systems",
author = "Jamie Roberts and Georgios Mastorakis and Brad Lazaruk and {Franco Aixela}, Santiago and Adam Stokes and Sara Bernardini",
year = "2021",
month = feb,
day = "16",
language = "English",
booktitle = "The 31st International Conference on Automated Planning and Scheduling (ICAPS 2021)",
}
```
