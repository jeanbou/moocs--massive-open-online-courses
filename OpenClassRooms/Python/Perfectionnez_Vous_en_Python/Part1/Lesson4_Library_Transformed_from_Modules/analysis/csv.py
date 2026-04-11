#! /usr/bin/env python3
# coding: utf-8

import os

def launch_analysis(data_file):
	directory = os.path.dirname(os.path.dirname(__file__)) # we get the right path.
	path_to_file = os.path.join(directory, "data", data_file) # with this path, we go inside the folder `data` and get the file.
	with open(path_to_file,"r") as f:
		preview = f.readline()
	print("Yeah! We managed to read the file. Here is a preview: {}".format(preview))

if __name__ == "__main__":
	print('Running main of launch_analysis...\n')
	launch_analysis('current_mps.csv')
else:
	print('You\'ve imported paritie.py as a library')