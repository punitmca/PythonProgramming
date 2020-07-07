def person(name, **data):
    print('Name',name)

    for i,j in data.items():
        print(i,j)

person('Punit', age=30, city='Delhi', mob=90888)