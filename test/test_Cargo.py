import pytest

from src.ships import Cargo

def testCargo1():
	cargo1_ = Cargo(-500,1,1000,500) # valor negativo, error
	with pytest.raises(ValueError):
		cargo1_.is_worth_it()

def testCargo2():
	cargo2_ = Cargo(100,0.5,5000,1000) # saqueable
	# como se que es >20 se que es saqueable
	assert(cargo2_.is_worth_it() >=20 ) == True

def testCargo3():
	cargo3_ = Cargo(1500,1,1000,500) # insaqueable (menos a 20), en este caso me quedaria -5000.
	with pytest.raises(ValueError):
		cargo3_.is_worth_it()
