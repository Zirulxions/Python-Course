def run():
    # my_dict = {'key' + str(value): value **2 for value in range(1,101) if value % 3 != 0}
    my_dict = {'key' + str(value): round(value ** (1/2),4) for value in range(1,1001)}
    
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         my_dict['key' + str(i)] = i**3

    
    print(my_dict)

if __name__ == '__main__':
    run()