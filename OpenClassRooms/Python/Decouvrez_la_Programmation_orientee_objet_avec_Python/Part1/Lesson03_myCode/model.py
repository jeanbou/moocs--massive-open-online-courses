import json

class Agent:
	def __init__(self, **agent_attributes):
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

#first_agent = Agent(0.8)
#second_agent = Agent(0)
#print(first_agent.say_hello("Ivan"),first_agent.agreeableness)

def main():
	for agent_attributes in json.load(open("agents-100k.json")):
		agent = Agent(**agent_attributes)
		# You can comment it
		#print(agent.agreeableness)
	agent.cities("France", "Paris", "Mollégès", "Bourg la Reine")
	agent.list_songs(adele_songs = ["Hello", "Someone like you"], backstreet_boys_songs = ["Larger than life", "I want it that way"])

main()