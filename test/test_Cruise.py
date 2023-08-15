import pytest

from src.ships import Cruise

def testCruise1():
	cruise1 = Cruise(100,5500,2000) # como es >20 -> saqueable 
	assert(cruise1.is_worth_it() >=20) == True 

def testCruise2():
	cruise2 = Cruise(3000,5000,500)  # (5000 - 500*1.5 - 3000*3.5)<0  
	with pytest.raises(ValueError):
		cruise2.is_worth_it()
		
def testCruise3():
	cruise3 = Cruise(-500,1000,500) # valor negativo, error
	with pytest.raises(ValueError):
		cruise3.is_worth_it()
