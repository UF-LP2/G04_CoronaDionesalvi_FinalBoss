from cShip import cShip
# cCruise es hijp de cShip
class cCruise(cShip):
	def __init__(self, passengers, draft, crew): 
		super().__init__(draft, crew) # usando super se hereda automaticamente los metodos del padre.
		# init__ es mi constructor 
		self.passengers = passengers # cantidad de pasajeros
		
	def calcularPeso(self):
		total = self.draft - self.crew * 1.5 # el total seria el peso neto del barco 
		aux = 0

		aux = self.passengers * 2.25 	# 2.25 de mis pasajeros
		total -= aux
		
		return aux
	
    # porq no alcanza con el from cShip import cShip para decir que es herencia???