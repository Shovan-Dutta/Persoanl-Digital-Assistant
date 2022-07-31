import random 

def coin():
	no = random.randint(0,1)
	if no == 0:
		return ('you got head')
	else:
		return('you got tails')


def dice():
	no = random.randint(1,6) 
	if no == 1: 
		return('you got 1')
	elif no == 2:
		return('you got 2')
	elif no == 3: 
		return('you got 3')
	elif no == 4: 
		return('you got 4') 
	elif no == 5: 
		return('you got 5') 
	elif no == 6: 
		return('you got 6') 
	print("\n")