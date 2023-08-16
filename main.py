import csv #import == include 

from src.ships import Ship 
from src.ships import Cargo
from src.ships import Cruise


def numerito(n): 
	try:
		float(n)
		return True
	except TypeError:
		return False
	  

def main() -> None:

	lista_de_barcos = [] 	

	# la r es de read, solo lectura
	with open('ships.csv','r') as fileCSV_: # fileCSV_ es el archivo abierto para leer
		fp = csv.reader(fileCSV_) # fp es el puntero dentro del archivo solo para la lectura

		next(fp) # next() hace avanzar una linea (fila) al lector de archivos, - se saltea los headers -
		cant = 0

		for row in fp: # row es la columna de la fila en la que esté ubicado el lector
			if row[2] == "" and row[3] == "" :
				if numerito(row[0]) and numerito(row[1]): # devuelve true si es un numero y false si no lo es
					barco1 = Ship(row[0], row[1])
					lista_de_barcos.append(barco1) # con append agrego un elemento a la lista
			
			elif row[2] != "" and row[3] == "" :
				if numerito(row[0]) and numerito(row[1]) and numerito(row[2]):
					crucero = Cruise(row[2], row[0], row[1]) # con esa condicion chequeo que el barco sea un crucero
					lista_de_barcos.append(crucero)

			elif row[2] != "" and row[3] != "" :
				if numerito(row[0]) and numerito(row[1]) and numerito(row[2]) and numerito(row[3]):
					buquedecarga = Cargo(row[2], row[3], row[0], row[1]) # barco de carga 
					lista_de_barcos.append(buquedecarga)

			else:
				print("Barco mal registrado")

if __name__ == "__main__":
  main()
