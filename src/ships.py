class Ship: #clase madre
	def __init__(self, draft, crew): 
		self.draft = draft # atributos-> self seria como mi puntero this
		self.crew = crew
			
	def calcularPeso(self): # polimorfico
		pesoAux = self.draft - self.crew*1.5 # draft peso total del barco y crew peso de la tripulacion
		if self.draft <0 or self.crew<0:
			raise ValueError("Error, paramentro negativo")
		return pesoAux 
			
	def is_worth_it(self):
		aux = self.calcularPeso()

		if(aux<20):
			raise ValueError("Insaqueable")
		return aux
	
# Cruise es hija de Ship
class Cruise(Ship):
	def __init__(self, passengers, draft, crew): 
		super().__init__(draft, crew) # usando super se hereda automaticamente los metodos del padre.
		# init__ es mi constructor 
		self.passengers = passengers # cantidad de pasajeros
		
	def calcularPeso(self):
		total = float(self.draft - (self.crew * 1.5)) # el total seria el peso neto del barco 
		aux = float(0.0)

		aux = self.passengers * 2.25 	# 2.25 de mis pasajeros
		total -= aux
		if self.draft<0 or self.crew<0 or self.passengers<0:
			raise ValueError("Error, paramentro negativo")
		return total
	
	def is_worth_it(self):
		aux = self.calcularPeso()

		if(aux<20):
			raise ValueError("Insaqueable")
		return aux
	
    # porq no alcanza con el from Ship import Ship para decir que es herencia???
   

class Cargo(Ship):
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
		if self.draft<0 or self.crew<0 or self.quality<0 or self.cargo<0:
			raise ValueError("Error, paramentro negativo")
		return total
	
	def is_worth_it(self):
		aux = self.calcularPeso()

		if(aux<20):
			raise ValueError("Insaqueable")
		return aux
