import time
name=''
password=''
counter=0
correct_name='Julie'

while True:
    print('Who are you? ')
    name=input()
    if name != correct_name:
        print('Get out '+name+', I will only speak with '+correct_name)
        time.sleep(1)
        continue
    print('Oh, hey '+name+'. What is the password? ')
    password=input()
    if password == 'hint':
        print("It's a weaponized fish")
        time.sleep(1)
    elif password == 'swordfish':
        print("You've solved my word puzzle!")
        break
    elif counter >0:
        print('maybe you need a hint?')
        response=input('Y/N: ')
        if response == 'y':
            print("It's a weaponized fish")
        else:
            print('Ok I guess')        
        time.sleep(1)
        continue
    else:
        print("You lied! You're not "+correct_name+'!')
        time.sleep(.5)
        print('I will only speak with '+correct_name)
        time.sleep(1)
        counter=counter+1
        continue
