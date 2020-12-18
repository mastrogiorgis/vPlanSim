#Jamie Roberts

import csv
import numpy as np


def read_plan(file):
	with open(file,mode = 'r') as csv_file:

		csv_reader = csv.reader(csv_file)
		read = []
		for row in csv_reader:
			for line in row:
				#do all text cleaning here
				line = line.replace('(','')
				line = line.replace(')','')
				line = line.replace(' ',',')
#				line = line.replace('c','')

				#split plan into list when text is clean
				read_line = line.split(',')
				read.append(read_line)

	return read




def clean(str):
	commands=[]
	data = []
	data_wash = []
	c = ''
	for char in str:
		if char == '(' or char  == ')':
			pass
		else:
			data.append(char)

	#print(data)
	for char in data:
		if char== ' ':
			data_wash.append(',')
		else:
			data_wash.append(char)
#	print(data_wash)
	for char in data_wash:
		word = False
		if char == ',':
			word = True
			commands.append(c)
		if char == '\n':
			word = True
			commands.append(c)
		elif char != ',':
			word = False
			c += char
		if word == True:
			c=''
	return commands


def import_plan_ax(filename):

	file = open(filename,'r')
	raw = []
	command_list = []
	with open(filename, mode ='r') as plan:
		reader = csv.reader(plan, delimiter = ' ', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
		for row in plan:
			raw.append(row)
		else:
			pass

	file.close()
	for command in raw:
		command_list.append(clean(command))
	plan = command_list
#	plan = interpet_ax(command_list)
	return plan
