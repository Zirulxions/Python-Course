def run():
    # my_list = [value ** 2 for value in range(1, 101) if value % 3 != 0]
    # squares = []
    # for i in range(1,101):
    #     squares.append(i**2)
    # print(squares)

    my_list = [value for value in range(1,10000) if value % 4 == 0 and value % 6 == 0 and value % 9 == 0]
    print(my_list)

if __name__ == '__main__':
    run()