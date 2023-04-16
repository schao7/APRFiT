import math

def S1(x, t, c):
	return (x * ((1-c)/t)) + c

def S2(x, t, c):
	return ((x * ((1-(c**2.0))/t)) + (c**2.0))**(1./2)

def S5(x, t, c):
	return ((x * ((1-(c**5.0))/t)) + (c**5.0))**(1./5)

def S10(x, t, c):
	return ((x * ((1-(c**10.0))/t)) + (c**10.0))**(1./10)

def S20(x, t, c):
	return ((x * ((1-(c**20.0))/t)) + (c**20.0))**(1./20)

def gp(x, t, c):
	return 2.0**((x * ((math.log(1,2.0) - math.log(c,2.0))/t)) + math.log(c,2.0))

def std(x, t, c):
	return 1


SCHEDULER_FUN = {
	'S1': S1,
	'S2': S2,
	'S5': S5,
	'S10': S10,
	'S20': S20,
	'gp': gp,
	'std': std
}
