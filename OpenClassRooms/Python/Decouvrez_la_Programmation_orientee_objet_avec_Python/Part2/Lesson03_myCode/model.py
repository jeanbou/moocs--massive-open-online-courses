import json
import math


class Agent:
	def __init__(self, position, **agent_attributes):
		self.position = position
		for attr_name, attr_value in agent_attributes.items():
			setattr(self, attr_name, attr_value)
	def say_hello(self, first_name):
		return "Start to running say_hello method, " + first_name + " , please wait "
	# Example of treatment tulips params
	def cities(country, *cities):
		print(country, cities)
		print("Type is ", type(cities))
	# Example of treatment tulips of tulips params
	def list_songs(**songs):
		print(songs)
		print("Type for tulips of tulips is ", type(songs))

class Position:
	def __init__(self, longitude_degrees, latitude_degrees):
		self.latitude_degrees = latitude_degrees
		self.longitude_degrees = longitude_degrees

	@property
	def longitude(self):
		# Longitude in radians
		return self.longitude_degrees * math.pi / 180

	@property
	def latitude(self):
		# Latitude in radians
		return self.latitude_degrees * math.pi / 180


#first_agent = Agent(0.8)
#second_agent = Agent(0)
#print(first_agent.say_hello("Ivan"),first_agent.agreeableness)

def main():
	for agent_attributes in json.load(open("agents-100k.json")):
		latitude = agent_attributes.pop("latitude")
		longitude = agent_attributes.pop("longitude")
		position = Position(latitude, longitude)
		agent = Agent(position,**agent_attributes)
		# You can comment it
		#print(agent.agreeableness)
		print(agent.position.longitude)
		print(agent.position.latitude)
		# Work with toolips of complex params
		agent.cities("France", "Paris", "Mollégès", "Bourg la Reine")
		agent.list_songs(adele_songs = ["Hello", "Someone like you"], backstreet_boys_songs = ["Larger than life", "I want it that way"])

main()