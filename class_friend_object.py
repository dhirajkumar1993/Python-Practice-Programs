class friend:
	pass

friend1 = friend()
friend2 = friend()

friend1.name = 'kapil'
friend1.age = 24
friend2.name = 'Abhishek'
friend2.age = 25

print (friend1.name.title() + " is " + str(friend1.age) + " years old.")
print (friend2.name.title() + " is " + str(friend2.age) + " years old.")