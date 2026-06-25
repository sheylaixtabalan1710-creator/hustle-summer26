# Sheyla Ixtabalan | Lab 3 | Red
# Ticket Strings 1
username = "SheylaIxtabalan"
print(len(username)) #PREDICT : 15 
print(username[0]) #PREDICT:S
print(username[14]) #PREDICT: n
#EXPLAIN: the last index is -1 because it reads up until the start of that letter
first =  "Sheyla"
Last = "Ixtabalan"
full = "Welcome to Loop, " + "@" + first + Last + "!"
print(full) #Welcome to Loop, @SheylaIxtabalan!
#PREDICT: Welcome to Loop, @SheylaIxtabalan!
print(f"Welcome to Loop, @{first}{Last}!") #PREDICT: Welcome to Loop, @SheylaIxtabalan!
#EXPLAIN : The f string felt easier because it was shorter and less complex.
#username[0] = "X"
print(username.upper()) #PREDICT : SHEYLAIXTABALAN 
#EXPLAIN: The error I saw was that it couldnt read the variable and the X got red highlighted. I thunk immutable means that it cant be chnaged or ran.
# Ticket Lists 2
feed = ["soccer","worldcup", "messi"]
print(len(feed)) #PREDICT: 3
print(feed[0]) #PREDICT: soccer
#EXPLAIN: I used the index 0 to print the first item on the list.
feed.append("love")
print(feed) #PREDICT: socer,worldcup,messi,love this fourth post will have an index of 3.
#EXPLAIN: It sits an an index of 3 becahse the first one sits at an index of 0.
feed.pop(0) #PREDICT: it removes the first post soccer.
feed.sort() #PREDICT: it will sort the list in alphabetical order. love,messi,worldcup
print(feed)
#EXPLAIN: I used the dot method to short in alphebetical order. I used the .pop() method to remove the first item from the list.
# Ticket Dictionaries 3
profile = {"username": "SheylaIxtabalan", "followers" : 67 , "verified" : True}
#profile[0] I think thsi will be and error because it is a dictionary and not a list.
print(profile)
print(profile ["followers"]) #PREDICT :67)
#PREDICT: The 67 follow count prints, I think profile[0] means that theres nothing in the profile.
#EXPLAIN: I think dictionaries look things off by key name so its more precise and knows what to look for.
profile["followers"] +=50
print(profile["followers"])
profile["bio"] = "I'm the goat"
print(profile)
print(profile.get("age")) #PREDICT: there wont be a pront of anything because the age doesnt exsist.
#EXPLAIN: I think its safer to use .get() than profile["age"] because it wont show an error it will just say if it exsists or not.
print(f"@" + profile["username"] + " has " + str(profile["followers"]) + " followers and " + str(len(feed)) + " posts." + " Top post : " + feed[0] +".")
#PREDICT: @SheylaIxtabalan has 117 followers and 3 posts. Top post : love.
#EXPLAIN: A list of every data structure I used to build this one line of code is a string, integer, boolean, list and dictionary.





