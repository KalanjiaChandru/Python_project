from promptclass_Day_4 import History

def repeat ():
	my_chat=History()
	
	while True:
		chat=input("Entet the prompt ")
		if chat.upper() == 'EXIT':
			print('Have good day')
			my_chat.clear_history()
			break
		my_chat.sendMessage(chat,"chandru")
		my_chat.get_history()
repeat()