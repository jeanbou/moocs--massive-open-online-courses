class Agent:
	def __init__(self,agreeableness_val):
		self.agreeableness = agreeableness_val
	def say_hello(self, first_name):
		return "Start to running say_hello method, " + first_name + " , please wait "

first_agent = Agent(0.8)
second_agent = Agent(0)
print(first_agent.say_hello("Ivan"),first_agent.agreeableness)