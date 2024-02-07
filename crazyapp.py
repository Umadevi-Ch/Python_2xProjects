def person(**data):
    #print(data)
    for k,v in data.items():
        if k == 'firstname':
            print(k, ' :', v)
        elif k == 'lastname':
            print(k, '  :', v)
        elif k == 'age':
            print(k, '       :', v)
        else:
            print(k,'  :', v)
    print("")
e=1
while e != '0':
    firstname = input("Enter your first name: ")
    lastname = input("Enter your last name: ")
    age = input("Enter your exact age: ")
    mobile = input("Enter your mobile: ")
    print("")
    person(firstname=firstname, lastname=lastname, age=age, mobileno=mobile)
    e = input("Enter 0 to exit or any key to continue: ")
    print("")