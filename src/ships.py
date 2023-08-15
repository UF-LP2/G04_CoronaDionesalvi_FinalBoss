class cShip: #clase madre
	def __init__(self, draft, crew): 
		self.draft = draft # atributos-> self seria como mi puntero this
		self.crew = crew
			
	def calcularPeso(self): # polimorfico
		pesoAux = self.draft - self.crew*1.5 # draft peso total del barco y crew peso de la tripulacion
		return pesoAux 
	
	def is_worth_it(self):
		if self.calcularPeso() >= 20: 
			return True # merece ser saqueado.
		else:
			return False # no merece ser saqueado.
		

# cCruise es hija de cShip
class cCruise(cShip):
	def __init__(self, passengers, draft, crew): 
		super().__init__(draft, crew) # usando super se hereda automaticamente los metodos del padre.
		# init__ es mi constructor 
		self.passengers = passengers # cantidad de pasajeros
		
	def calcularPeso(self):
		float(total = self.draft - (self.crew * 1.5)) # el total seria el peso neto del barco 
		float(aux = 0.0)

		aux = self.passengers * 2.25 	# 2.25 de mis pasajeros
		total -= aux
		
		return aux
	
    # porq no alcanza con el from cShip import cShip para decir que es herencia???
   

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

