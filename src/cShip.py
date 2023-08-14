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