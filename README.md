# vPlanSim
An Open Source Graphical Interface for the Visualisation and Simulation of AI Systems


Features of vPlanSim


The user defines the 3D geometry of the scene by adjusting the external and internal walls.

![image](https://user-images.githubusercontent.com/23278410/110217077-14985600-7eaa-11eb-89f5-fbf00ac46937.png)

The tool offers several viewing angles and viewing helper functions such as the axis and origin of the 3D visual space, a continuous grid annotating the ground, the coordinates of the walls and the floor within the walls.

![image](https://user-images.githubusercontent.com/23278410/110217184-a99b4f00-7eaa-11eb-994a-a39f50cb7b33.png)

The user can delete the entire scene or specific blocks from the walls and can also add obstacles on the floor. Also, the geometry can be adjusted using the following menu to undo/redo wall creation, obstacles insertion or block deletion.

![image](https://user-images.githubusercontent.com/23278410/110217307-32b28600-7eab-11eb-9edd-d8098861fcdf.png)

The planning menu holds the generation of PDDL based on a particular domain and using the above geometry. The user can select the coordinates of goals, entries and elements, name the problem name, then generate and preview the PDDL problem file.

![image](https://user-images.githubusercontent.com/23278410/110217433-f3386980-7eab-11eb-858a-c1c5457465ea.png)

Finally, the user can visually simulate step-by-step the plan (after solving the PDDL problem).

![image](https://user-images.githubusercontent.com/23278410/110217536-69d56700-7eac-11eb-96b6-da1d64e7174c.png)
