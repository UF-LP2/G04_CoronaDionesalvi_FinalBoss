import pytest

from src.ships import Ship

# Caso de barco generico saqueable
def testShip1():
	ship1_ = Ship(3500,2000) # como es = a 500 (2000 - 1000*1.5 = 500)
	assert(ship1_.is_worth_it() == 500) == True # podria poner >=20

def testShip2():
	ship2_ = Ship(-200,350) # error
	with pytest.raises(ValueError):
		ship2_.is_worth_it()

def testShip3():
	ship3_ = Ship(-250,550) # error
	with pytest.raises(ValueError):
		ship3_.is_worth_it()