import os

def palindromo(palabra):
	palabra_original = palabra
	palabra = palabra.replace(' ','').upper()
	if palabra == palabra[::-1]:
		return "Es palindromo: " + palabra_original
	else:
		return "No es palindromo: " + palabra_original

def potencias(ciclo):
	acumulador = 0
	numero = int(input("Ingrese un numero: "))
	while acumulador <= ciclo:
		print(str(numero) + " elevado a " + str(acumulador) + " es igual a: " + str(numero**acumulador))
		acumulador += 1
	print("Finalizadas las potencias")

def bienvenida():
	print("Seleccione una opcion:")
	print("0- Salir")
	print("1- Palindromos")
	print("2- Potencias (Sub-bucle)")
	return input("Opcion: ")

def run():
	menu = True
	while menu == True:
		opcion = bienvenida()
		if int(opcion) == 0:
			print("Hasta luego...")
			menu = False
			break
		elif int(opcion) == 1:
			palabra = input("Ingrese una palabra: ")
			print(palindromo(palabra))
			del palabra
		elif int(opcion) == 2:
			recuento = int(input("Ingrese la cantidad de repeticiones: "))
			potencias(recuento)
		else:
			print("La opcion: " + opcion + " no es una opcion valida.")
		input("Presione una tecla para continuar...")
		os.system('cls')


if __name__ == '__main__':
	run()