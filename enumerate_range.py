import random

random_bits = 0
for i in range(64):
	if random.randint(0,1):

		random_bits = 1 <<i

flavor_list = ['vanilla' , 'chocolate' , 'pecan' , 'strawberry']
for flavor in flavor_list:
	print('%s is delicious' %flavor)

'''' We will use range function'''

print('Done using range')
for i in range(len(flavor_list)):
	flavor = flavor_list[i]
	print('%d: %s' % (i+1, flavor))

''' Now we will use enumerate function'''

print('Done using enumeration')
for i , flavor in enumerate(flavor_list):
	print('%d: %s' %(i + 1 , flavor))
