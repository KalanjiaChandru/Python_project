from collections import deque
# List actions

# movies=['visvasma','Jey Jey','KGF','mersal','MSD Untold story']
# movies[2]='vali'
# movies.append('gilli')
# movies.append('Tamil padam')
# print(movies)

# Create a dictionary for a student: name, age, grade, city.
# Update grade.
# Add "skills": ["python", "git"].
# Print all keys and values.

# student={'name':'chandru','age':'26','grade':'A','city':'Tenkasi'}
# student['grade']='A+'
# student['skills']=['python','git']
# print(student)

# numbers = set({1,2,3,4,4,5,5,6})
# numbers.add(7)
# numbers.remove(4)
# print(numbers)


# colour=('red','blue','green')
# print(colour[0])
# convertion=list(colour)
# convertion.append('yellow')
# backto=tuple(convertion)
# print(backto)

recent_songs=deque(['vathi comming','Ennode ne iruthal ','neum nanum sentha selum nerama'],maxlen=3)

print('Initial list',list(recent_songs))

recent_songs.append('i am barby girl')

print(list(recent_songs))

# recent_songs.append('po indru ne aga ')
# if len(recent_songs)>3:
#     del recent_songs[0]
# print(recent_songs)    

search ='friend request'

notifications = ["message", "friend request", "tagged photo"]
notifications.append('Comment')
if search in notifications:
    idx=notifications.index(search)
    notifications[idx]='follow request'
notifications.pop(0)
print(notifications)
