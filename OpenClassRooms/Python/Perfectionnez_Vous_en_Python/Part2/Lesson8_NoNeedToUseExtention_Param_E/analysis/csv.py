#! /usr/bin/env python3
# coding: utf-8

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class SetOfParliamentMembers:
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return "SetOfParliamentMember: {} members".format(len(self.dataframe))

	def total_mps(self):
		return len(self.dataframe)
	
	def data_from_csv(self, csv_file):
		self.dataframe = pd.read_csv(csv_file, sep=";")

	def data_from_dataframe(self, dataframe):
		self.dataframe = dataframe

	def display_chart(self):
		data = self.dataframe
		female_mps = data[data.sexe == "F"]
		male_mps = data[data.sexe == "H"]
		counts = [len(female_mps), len(male_mps)]
		counts = np.array(counts)
		nb_mps = counts.sum()
		proportions = counts / nb_mps
		labels = ["Female ({})".format(counts[0]), "Male ({})".format(counts[1])]
		fig, ax = plt.subplots()
		ax.axis("equal")
		ax.pie(proportions,labels=labels,autopct="%1.1f pourcents")
		plt.title("{} ({} MPs)".format(self.name, nb_mps))
		plt.show()

	def split_by_political_party(self):
		result = {}
		data = self.dataframe
		all_parties = data["parti_ratt_financier"].dropna().unique()
		for party in all_parties:
			data_subset = data[data.parti_ratt_financier == party]
			subset = SetOfParliamentMembers('MPs from party "{}"'.format(party))
			subset.data_from_dataframe(data_subset)
			result[party] = subset
		return result

def launch_analysis(data_file, by_party = False, info = False ):
	sopm = SetOfParliamentMembers("All MPs")
	sopm.data_from_csv(os.path.join("data",data_file))
	sopm.display_chart()
	# Lesson 7 Partie No. 2
	if info:
		print(sopm.total_mps())
		print("Printing the result of override of __repr__")
		print(sopm)
	if by_party:
		for party, s in sopm.split_by_political_party().items():
			s.display_chart()
	# old code of analysis
	directory = os.path.dirname(os.path.dirname(__file__)) # we get the right path.
	path_to_file = os.path.join(directory, "data", data_file) # with this path, we go inside the folder `data` and get the file.
	try:
		with open(path_to_file,"r") as f:
			preview = f.readline()
			print("Yeah! We managed to read the file. Here is a preview: {}".format(preview))
	except FileNotFoundError as e:
		print("Ow :( The file was not found. Here is the original message of the exception :", e)
	except:
		print('Destination unknown')


if __name__ == "__main__":
	print('Running main of launch_analysis...\n')
	launch_analysis('current_mps.csv')
else:
	print('You\'ve imported paritie.py as a library')