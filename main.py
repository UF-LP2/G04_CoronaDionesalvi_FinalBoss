import csv #import == include 

from src.ships import Ship 
from src.ships import Cargo
from src.ships import Cruise


def esNumero(n):
        try:
		            float(n)
                return True
	      except TypeError:
		            return False
	  

def main() -> None:

lista_de_barcos = [] 

	# la r es de read, solo lectura
with open('ships.csv','r') as archivoBarcos:
		lectorBarcos = csv.reader(archivoBarcos)

		
		next(lectorBarcos) # next() hace avanzar una linea (fila) al lector de archivos, - se saltea los headers -
		cant = 0

	
		for row in lectorBarcos: # row es la columna de la fila en la que esté ubicado el lector
			if row[2] == "" and row[3] == "" :
				if esNumero(row[0]) and esNumero(row[1]):
					barco1 = Ship(row[0], row[1])
					lista_de_barcos.append(barco1) # con append agrego un elemento a la lista
			
			elif row[2] != "" and row[3] == "" :
				if esNumero(row[0]) and esNumero(row[1]) and esNumero(row[2]):
					barco2 = Cruise(row[2], row[0], row[1]) # con esa condicion chequeo que el barco sea un crucero
					lista_de_barcos.append(barco2)

			elif row[2] != "" and row[3] != "" :
				if esNumero(row[0]) and esNumero(row[1]) and esNumero(row[2]) and esNumero(row[3]):
					barco3 = Cargo(row[2], row[3], row[0], row[1]) # barco de carga 
					lista_de_barcos.append(barco3)

			else:
				cant += 1

if __name__ == "__main__":
  main()
