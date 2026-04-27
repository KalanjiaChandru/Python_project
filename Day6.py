from promptclass_Day_4 import Aiparson
import json


try:
	value = input('Enter what bot do you want me to code 1.coading_bot || 2.comedy_bot')
	name=input('Enter your name ')
	skills=input('Enter you skills ').split(',')
	if value == "1":
		with open('storage.json', 'r') as store:
			history = json.load(store)
			# Add your file handling logic here
			pass
		coading_bot = Aiparson(name, skills,history)
	
		pass
	elif value == "2":
		with open('storage.json','r') as store:
			history=json.load(store)
			pass
		comedy_bot = Aiparson(name, skills,history)
	convert = int(value)
	while True:
		if convert == 1:
			value = input('Enter what you want 1.prompt||2.history||3.Exit')
			con = int(value)
			if con == 1:
				prompt = input("Enter the prompt you want ")
				coading_bot.addMessage(prompt,'coading_bot')
				pass

			pass
		elif con ==2:
			coading_bot.viewHistory('coading_bot')
		elif con == 3:
			coading_bot.Exit('coading_bot')
			pass
		elif convert ==2:
			
			pass
except Exception as e:
	print(f"An error occurred: {e}")

