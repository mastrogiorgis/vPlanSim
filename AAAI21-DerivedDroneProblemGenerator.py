#!/usr/bin/env python3
import sys
import random
agents=int(sys.argv[1]) 
gridSize=int(sys.argv[2])
goalPositions=int(sys.argv[3])
inputSeed=int(sys.argv[4])
seed=inputSeed+1
random.seed(seed)

domain_name="domain_Derived_Drones_C"+str(gridSize)+"_D"+str(agents)
domain_file_name=domain_name+".pddl"
exp = "{}".format(domain_file_name)
domain = open(exp,"w")
#domain = open("domain_hybrid_no_axiom.pddl", "w")

canonical_angles_2D_names=["plusX","plusY"]
angles_3D_names=["plusX","minusX","plusY","minusY","plusZ","minusZ"]
angles_2D_names=["plusX","minusX","plusY","minusY"]

#Functions

def forbid(orig_x,orig_y,orig_z):
    for var in range(agents):
        domain.write("\n\t\t\t(not (at_agent s"+str(var)+" ?"+orig_x+" ?"+orig_y+" ?"+orig_z+"))")

def forbid_bookmark(orig_x,orig_y,orig_z):
    domain.write("\n\t\t(not (occupied ?"+orig_x+" ?"+orig_y+" ?"+orig_z+"))")

def forbid_axiom(orig_x,orig_y,orig_z):
    domain.write("\n\t\t(not (exists (?s - agent)")
    domain.write("\n\t\t\t(at_agent ?s ?x2 ?y2 ?z2)")
    domain.write("\n\t\t))")
def forbid_derived(orig_x,orig_y,orig_z):
    for var in range(agents):
        domain.write("\n\t\t(not_agent s"+str(var)+" ?"+orig_x+" ?"+orig_y+" ?"+orig_z+")")


def include(orig_x,orig_y,orig_z):
    domain.write("\n\t\t(or ")
    for var in range(agents):
        domain.write("\n\t\t\t(at_agent1 s"+str(var)+" ?"+orig_x+" ?"+orig_y+" ?"+orig_z+")")
        domain.write("\n\t\t\t(at_agent2 s"+str(var)+" ?"+orig_x+" ?"+orig_y+" ?"+orig_z+")")
        domain.write("\n\t\t\t(at_agent3 s"+str(var)+" ?"+orig_x+" ?"+orig_y+" ?"+orig_z+")")
        domain.write("\n\t\t\t(at_agent4 s"+str(var)+" ?"+orig_x+" ?"+orig_y+" ?"+orig_z+")")
    domain.write("\n\t\t) ")
def includeAng(orig_x,orig_y,orig_z,angle,agent):
        domain.write("\n\t\t\t(at_agent1 ?"+str(agent)+" ?"+orig_x+" ?"+orig_y+" ?"+orig_z+")")
        domain.write("\n\t\t\t(angle_agent ?"+str(agent)+" "+angle+")")
def includeAngAnyStrut(orig_x,orig_y,orig_z,angle):
    return
    domain.write("\n\t\t(or ")
    for agent in range(agents):
        domain.write("\n\t\t\t(and ")
        domain.write("\n\t\t\t\t(at_agent1 s"+str(agent)+" ?"+orig_x+" ?"+orig_y+" ?"+orig_z+")")
        domain.write("\n\t\t\t\t(angle_agent s"+str(agent)+" "+angle+")")
        domain.write("\n\t\t\t) ")

    domain.write("\n\t\t) ")

def checkAgent(orig_x,orig_y,orig_z,ang,agent):
    if ang=="0ang":
        domain.write("\n\t\t\t(at_agent1 ?"+str(agent)+" ?"+str(orig_x)+" ?"+orig_y+" ?"+orig_z+")")
        domain.write("\n\t\t\t(at_agent2 ?"+str(agent)+" ?p1 ?"+orig_y+" ?"+orig_z+")")
        domain.write("\n\t\t\t(at_agent3 ?"+str(agent)+" ?p2 ?"+orig_y+" ?"+orig_z+")")
        domain.write("\n\t\t\t(at_agent4 ?"+str(agent)+" ?p3 ?"+orig_y+" ?"+orig_z+")")
    if ang=="90ang":
        domain.write("\n\t\t\t(at_agent1 ?"+str(agent)+" ?"+str(orig_x)+" ?"+orig_y+" ?"+orig_z+")")
        domain.write("\n\t\t\t(at_agent2 ?"+str(agent)+" ?"+str(orig_x)+" ?p1 ?"+orig_z+")")
        domain.write("\n\t\t\t(at_agent3 ?"+str(agent)+" ?"+str(orig_x)+" ?p2 ?"+orig_z+")")
        domain.write("\n\t\t\t(at_agent4 ?"+str(agent)+" ?"+str(orig_x)+" ?p3 ?"+orig_z+")")
    if ang=="450ang":
        domain.write("\n\t\t\t(at_agent1 ?"+str(agent)+" ?"+str(orig_x)+" ?"+orig_y+" ?"+orig_z+")")
        domain.write("\n\t\t\t(at_agent2 ?"+str(agent)+" ?"+str(orig_x)+" ?"+orig_y+" ?p1)")
        domain.write("\n\t\t\t(at_agent3 ?"+str(agent)+" ?"+str(orig_x)+" ?"+orig_y+" ?p2)")
        domain.write("\n\t\t\t(at_agent4 ?"+str(agent)+" ?"+str(orig_x)+" ?"+orig_y+" ?p3)")
def insertAgent(orig_x,orig_y,orig_z,agent):
    domain.write("\n\t\t\t(at_agent ?"+str(agent)+" ?"+str(orig_x)+" ?"+orig_y+" ?"+orig_z+")")
    #domain.write("\n\t\t\t(occupied ?"+str(orig_x)+" ?"+orig_y+" ?"+orig_z+")")
def notAgent(orig_x,orig_y,orig_z,ang,agent):
    if ang=="0ang":
        domain.write("\n\t\t\t(not (at_agent1 s"+str(agent)+" ?"+str(orig_x)+" ?"+orig_y+" ?"+orig_z+"))")
        domain.write("\n\t\t\t(not (at_agent2 s"+str(agent)+" ?p1 ?"+orig_y+" ?"+orig_z+"))")
        domain.write("\n\t\t\t(not (at_agent3 s"+str(agent)+" ?p2 ?"+orig_y+" ?"+orig_z+"))")
        domain.write("\n\t\t\t(not (at_agent4 s"+str(agent)+" ?p3 ?"+orig_y+" ?"+orig_z+"))")
def removeAgent(orig_x,orig_y,orig_z,agent):
    domain.write("\n\t\t\t(not (at_agent ?"+str(agent)+" ?"+str(orig_x)+" ?"+orig_y+" ?"+orig_z+"))")
    #domain.write("\n\t\t\t(not (occupied ?"+str(orig_x)+" ?"+orig_y+" ?"+orig_z+"))")
def removeAgentOut(agent):
    domain.write("\n\t\t\t(not (at_agent ?"+str(agent)+" outC outC outC))")


def forbidArea(orig_x,orig_y,orig_z,ang):
    forbid(orig_x,orig_y,orig_z)
    if ang=="0ang":
        forbid("p4",orig_y,orig_z)
        forbid("p5",orig_y,orig_z)
        forbid("p6",orig_y,orig_z)
    if ang=="90ang":
        forbid(orig_x,"p4",orig_z)
        forbid(orig_x,"p5",orig_z)
        forbid(orig_x,"p6",orig_z)
    if ang=="450ang":
        forbid(orig_x,orig_y,"p4")
        forbid(orig_x,orig_y,"p5")
        forbid(orig_x,orig_y,"p6")

#Types
domain.write("(define (domain ConnectR_3D_Sparse_Derivedless_NoIntrusion)")
domain.write("\n\t(:requirements :adl :typing)")
domain.write("\n\t(:types coord - object agent - object)")
domain.write("\n\t(:constants outC - coord ")

for var in range(agents):
    domain.write("s%d "%var)
domain.write("- agent)\n");


domain.write("\n\t(:predicates")
domain.write("\n\t\t(at_agent ?r - agent ?x ?y ?z - coord)")
domain.write("\n\t\t(not_agent ?r - agent ?x ?y ?z - coord)")

#domain.write("\n\t\t(occupied ?x ?y ?z - coord)")
domain.write("\n\t\t;;NOTE:IF MORE THAN ONE APERTURE NEEDED, NEED TO CREATE AN APERTURE OBJECT TO LINK THEM")

domain.write("\n\t\t(at_aperture ?x ?y ?z - coord)")
domain.write("\n\t\t(plus_four ?c1 ?c2 - coord)")
domain.write("\n\t\t(plus_one ?c1 ?c2 - coord)")
domain.write("\n\t\t(plus_three ?c1 ?c2 - coord)")

#domain.write("\n\t\t(dyn_at ?x ?y ?z - coord)")
#domain.write("\n\t\t(agent_less ?c1 ?c2 - countable)")

#domain.write("\n\t\t(is_outside ?r1 - agent)")


domain.write("\n\t)")
domain.write("\n(:derived (not_agent ?rmov - agent ?x2 ?y2 ?z2 - coord)")
domain.write("\n\t(exists (?x1 ?y1 ?z1 - coord)")
domain.write("\n\t\t(and")
domain.write("\n\t\t\t(at_agent ?rmov ?x1 ?y1 ?z1)")
domain.write("\n\t\t\t(or")
domain.write("\n\t\t\t\t(not (= ?x1 ?x2))")
domain.write("\n\t\t\t\t(not (= ?y1 ?y2))")
domain.write("\n\t\t\t\t(not (= ?z1 ?z2))")
domain.write("\n\t\t\t)")
domain.write("\n\t\t)")
domain.write("\n\t)")
domain.write("\n)")


domain.write("\n(:action insert")
domain.write("\n\t:parameters (?rmov - agent ?x2 ?y2 ?z2 - coord)")

domain.write("\n\t:precondition (and")

domain.write("\n\t\t(at_agent ?rmov outC outC outC)")
domain.write("\n\t\t(not (= ?x2 outC))")
domain.write("\n\t\t(not (= ?y2 outC))")
domain.write("\n\t\t(not (= ?z2 outC))")

domain.write("\n\t\t;;agent has to be outside for insert")
domain.write("\n\t\t;;aperture exists")

domain.write("\n\t\t(at_aperture ?x2 ?y2 ?z2)")
#Collision check
forbid_derived("x2","y2","z2")

domain.write("\n\t)")
domain.write("\n\t:effect (and")
removeAgentOut("rmov")
insertAgent("x2","y2","z2","rmov")

#domain.write("\n\t(increase (total-cost) 1)")
domain.write("\n\t)")
domain.write("\n)\n")

for ang in angles_3D_names:
    domain.write("\n\t(:action walk_%s" % ang)
    domain.write("\n\t:parameters (?rmov - agent ?x1 ?y1 ?z1 ?x2 ?y2 ?z2 - coord)")
    domain.write("\n\t:precondition (and")

    domain.write("\n\t\t(at_agent ?rmov ?x1 ?y1 ?z1)")
    forbid_derived("x2","y2","z2")

    if ang=="plusX":
        domain.write("\n\t\t(= ?y2 ?y1)")
        domain.write("\n\t\t(= ?z2 ?z1)")
        domain.write("\n\t\t(plus_one ?x1 ?x2)")
    elif ang=="minusX":
        domain.write("\n\t\t(= ?y2 ?y1)")
        domain.write("\n\t\t(= ?z2 ?z1)")
        domain.write("\n\t\t(plus_one ?x2 ?x1)")
    elif ang=="plusY":
        domain.write("\n\t\t(= ?x2 ?x1)")
        domain.write("\n\t\t(= ?z2 ?z1)")
        domain.write("\n\t\t(plus_one ?y1 ?y2)")
    elif ang=="minusY":
        domain.write("\n\t\t(= ?x2 ?x1)")
        domain.write("\n\t\t(= ?z2 ?z1)")
        domain.write("\n\t\t(plus_one ?y2 ?y1)")
    elif ang=="plusZ":
        domain.write("\n\t\t(= ?x2 ?x1)")
        domain.write("\n\t\t(= ?y2 ?y1)")
        domain.write("\n\t\t(plus_one ?z1 ?z2)")
    elif ang=="minusZ":
        domain.write("\n\t\t(= ?x2 ?x1)")
        domain.write("\n\t\t(= ?y2 ?y1)")
        domain.write("\n\t\t(plus_one ?z2 ?z1)")

    domain.write("\n\t\t)")
    domain.write("\n\t:effect (and")
    removeAgent("x1","y1","z1","rmov")
    insertAgent("x2","y2","z2","rmov")
    domain.write("\n\t)")
    domain.write("\t\n)\n")

domain.write("\n)\n")

domain.close()


###########################
#PROBLEM FILE
###########################

problem_name="problem_Derived_Drones_C"+str(gridSize)+"_D"+str(agents)+"_G"+str(goalPositions)+"_S"+str(seed)
problem_file_name=problem_name+".pddl"
exp = "{}".format(problem_file_name)
problem = open(exp,"w")
problem.write("(define (problem "+problem_name+") (:domain ConnectR_3D_Sparse_Derivedless_NoIntrusion)\n  (:objects \n");

problem.write("\t")
for pos in range(gridSize):
    problem.write("c%d "%pos)
problem.write(" - coord\n")
problem.write(")\n")
problem.write("  (:init\n\t")

for coord in range(gridSize-1):
    to_coord=coord+1
    problem.write("(plus_one c%i c%i) "%(coord,to_coord))
problem.write("\n")

for coord in range(gridSize-3):
    to_coord=coord+3
    problem.write("(plus_three c%i c%i) "%(coord,to_coord))
problem.write("\n")

for coord in range(gridSize-4):
    to_coord=coord+4
    problem.write("(plus_four c%i c%i) "%(coord,to_coord))
problem.write("\n")

problem.write("\n\t\t(at_aperture c0 c0 c0)")


for var in range(agents):
    problem.write("\t(at_agent s%i outC outC outC)\n"%var)
#problem.write("\t(at_agent1 s%i c0 c0 c1)\n"%(agents-2))
#problem.write("\t(at_agent2 s%i c1 c0 c1)\n"%(agents-2))
#problem.write("\t(at_agent3 s%i c2 c0 c1)\n"%(agents-2))
#problem.write("\t(at_agent4 s%i c3 c0 c1)\n"%(agents-2))
#problem.write("\t(angle_agent s%i 0ang)\n"%(agents-1))

#closing init
problem.write(")\n")

problem.write("(:goal (and\n")
#problem.write("\t(at_agent s%i c0 c0 c1)\n"%(agents-1))a
#for var in range(agents):
chosenGoals=[]
for var in range(goalPositions):
    while True:
        goalX=random.randint(0,gridSize-1)
        goalY=random.randint(0,gridSize-1)
        goalZ=random.randint(0,gridSize-1)
        randomPosition=str(goalX)+"-"+str(goalY)+"-"+str(goalZ)
        if randomPosition in chosenGoals:
            continue
        else:
            chosenGoals.append(randomPosition)
            problem.write("\t(at_agent s%i c%i c%i c%i)\n"%(var,goalX,goalY,goalZ))
            break
problem.write("))\n")
problem.write(")\n")
problem.close()
