import random

def busqueda_lineal(lista,objetivo):
	for elemento in lista:
		if elemento == objetivo:
			return True
	return False

def run():
	tamano_de_la_lista = int(input('De que tamano sera la lista? R: '))
	objetivo = int(input('Que numero quieres encontrar? R: '))

	lista = [random.randint(0,100) for i in range(tamano_de_la_lista)]

	encontrado = busqueda_lineal(lista,objetivo)
	print(lista)
	print(f'El elemento Objetivo {objetivo} {" Esta " if encontrado else " no esta "} en la lista')

if __name__ == '__main__':
	run()