
def run():
    my_list = [1,"Hello",True,4.5]
    my_dict = {"firstname":"Javier","lastname":"Delgado"}

    super_list = [
        {"firstname":"Javier","lastname":"Delgado"},
        {"firstname":"Rafael","lastname":"Ramirez"},
        {"firstname":"Ernesto","lastname":"Rincon"},
        {"firstname":"Vicky","lastname":"Fuenmayor"},
        {"firstname":"Exdihann","lastname":"Finol"},
    ]
    super_dict = {
        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-1,-2,0,1,2],
        "floating_nums":[1.1,4.5,6.43,1.54],
    }
    print("============================================")

    for key,value in super_dict.items():
        print(f'{key} - {value}')

    print("============================================")

    for i in range(len(super_list)):
        print(super_list[i])
        print(super_list[i].keys(), "-", super_list[i].values())
        print(super_list[i].get('firstname'), "-", super_list[i].get('lastname'))
        print("======")

    print("============================================")


if __name__ == '__main__':
    run()