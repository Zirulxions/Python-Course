def divisors(num):
    try:
        assert int(num) != 0, "El numero no puede ser cero"
        assert int(num) > 0, "El numero no puede ser negativo"
        diviors = [value for value in range(1,num + 1) if num % value == 0]
        return diviors
    except AssertionError as err:
        print(err)
        return False

def run():
    try:
        num = input("ingresa un numero: ")
        assert num.isnumeric(), "Debes ingresar un numero"
        print(divisors(int(num)))
    except AssertionError as err:
        print(err)
    finally:
        print("Finalizado.")

if __name__ == '__main__':
    run()