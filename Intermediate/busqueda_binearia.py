import random
import os

def busqueda_binaria(lista, comienzo, final, objetivo):
	if comienzo > final:
		return False

	medio = (comienzo + final) // 2
	print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
	# print(f'Medio: {medio} \nObjetivo: {objetivo} \nComienzo: {comienzo} \nFinal: {final - 1} \n====================')

	if lista[medio] == objetivo:
		return True
	elif lista[medio] < objetivo:
		return busqueda_binaria(lista, medio + 1, final, objetivo)
	# elif lista[medio] > objetivo:
	else:
		return busqueda_binaria(lista, comienzo, medio - 1, objetivo)


def run():
	tamano_de_la_lista = int(input('De que tamano sera la lista? R: '))
	objetivo = int(input('Que numero quieres encontrar? R: '))
	lista = sorted([random.randint(0,100) for i in range(tamano_de_la_lista)])
	os.system('cls')
	encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
	print(lista)
	print('====================')
	print(f'El elemento Objetivo {objetivo} {"ESTA" if encontrado else "NO ESTA"} en la lista')

if __name__ == '__main__':
	run()