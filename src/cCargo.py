from cShip import cShip

class cCargo(cShip):
	def __init__(self, cargo, quality, draft, crew):
		super().__init__(draft, crew)
		self.cargo = cargo
		self.quality = quality

	def calcularPeso(self):
		total = float( self.draft - self.crew * 1.5 )
		aux = 0.0 # asi lo toma como un float 

		if self.quality == 1:
			aux = 3.5
		elif self.quality == 0.5:
			aux = 2
		elif self.quality == 0.25:
			aux = 0.5
		else:
			raise ValueError("Error") # raise es un throw

		total -= (self.cargo * aux)
		return total
	
    