###############################
# Object oriented programming demo
###############################

# Define a person class
class Person:
	def __init__(self, name, height, weight):
		self.name = name
		self.height = height
		self.weight = weight

	def talk(self, stuff):
		print("%s says '%s'" % (self.name, stuff))

	def stats(self):
		print("My name is %s, I'm %s feet tall, and I weigh %s lbs" % (self.name, self.height, self.weight))

# Create a person object, bobby
bobby = Person("Bobby Joe", 6.1, 215)
# Make bobby do things
bobby.talk("I'ma head up the bayou and grab me some crawfish!")
bobby.stats()
print(bobby.name)

# Create a Man class, that inherits from our Person class
# I'm going to use the "random" module in the Man class, so I'll have to import it first
import random

class Man(Person):
	def __init__(self, name, height, weight):
		Person.__init__(self, name, height, weight)
		self.gender = 'Male'

	def drunkTalk(self, stuff):
		stuffA = list(stuff)
		stuffB = []

		for char in stuffA:
			stuffB.append(char)
			x = random.randint(1,10)
			if x <= 3 and char.isalpha():
				for y in range(x):
					stuffB.append(char)

		self.talk("".join(stuffB))

# Make some Man and Person objects, alex and fred, and have them do stuff
alex = Man("Alex Malex", 5.9, 170)
alex.drunkTalk("oh god I had way too many beers, I'm hammered!")
alex.talk("oh god I had way too many beers, I'm hammered!")

fred = Person("Fred Frogurt", 5.5, 150)
fred.drunkTalk("oh god I had way too many beers, I'm hammered!")
fred.talk("oh god I had way too many beers, I'm hammered!")


###############################
# HTTP demo
###############################

telnet www.google.ca 80
GET / HTTP/1.1

telnet www.yashley2014.com 80
GET / HTTP/1.0
GET /fakepath HTTP/1.0