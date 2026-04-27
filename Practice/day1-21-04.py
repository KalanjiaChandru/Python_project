raw_logs = [
    ("user_1", "Hello, how are you?", 0.9),
    ("user_2", "I need help with code.", 0.8),
    ("user_1", "Explain quantum physics.", 0.95),
    ("user_3", "Inappropriate content here.", 0.2),
    ("user_2", "Write a poem about AI.", 0.7),
]

uniqueuser=set(raw_logs)
filterscore=filter(lambda y:y[2]>0.5,uniqueuser)
user,message,score=filterscore
outputvalue={}
if user not in outputvalue:
    outputvalue[user]=[]
outputvalue[user].append(message)

