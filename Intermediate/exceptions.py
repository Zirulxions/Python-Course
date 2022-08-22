def divisors(num):
    try:
        if num == 0:
            raise ValueError("No se admite cero")
        elif num < 0:
            raise ValueError("No se admite numeros negativos")
        else:
            diviors = [value for value in range(1,num + 1) if num % value == 0]
        return diviors
    except ValueError as ve:
        print(ve)
        return False

def run():
    try:
        print(divisors("aa"))
    except:
        print("No se pueden ingresar letras")
    finally:
        pass

if __name__ == '__main__':
    run()