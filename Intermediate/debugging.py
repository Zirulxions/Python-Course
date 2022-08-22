def divisros(num):
    # diviors = [value for value in range(1,num + 1) if num % value == 0]
    diviors = []
    for i in range(1,num+1):
        if num % i == 0:
            divisros.append(i)
    return diviors

def run():
    num = int(input("Ingrese un numero: "))
    print(divisros(num))
    print("BAI BAI")

if __name__ == '__main__':
    run()