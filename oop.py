class Animal:
	def __init__(self,name,age,color,size):
		self.name = name 
		self.age = age
		self.color = color	
		self.size = size		
	def print_all(self):
		print(self.name)
		print(self.age)
		print(self.color)
		print(self.size)
	def eat (self,food):
		print(" the Animal "+self.name+" is eating "+food)
	def dream (self,dream):
		print(" the Animal "+self.name+" is dreaming "+dream)

dog=Animal("sadek",22,"yellow","tiny")
lion = Animal("nofar",1,"orenge", "big")
#SHoRTCUT 
#dog.print_all()
#lion.print_all()
dog.eat("pizza")
dog.dream("on amitay")
lion.eat("pizza")
lion.dream("on amitay")
#print(dog.name)
#print(dog.age)
#print(dog.color)
#print(dog.size)

