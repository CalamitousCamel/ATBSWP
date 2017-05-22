def collatz(number):
    newnumber=number
    while newnumber != 1:
        if newnumber %2 == 0:
            newnumber=newnumber//2
            print(newnumber)
        else:
            newnumber= 3*newnumber+1
            print(newnumber)
try:  
    number = int(input('Enter a nmumber: '))
    collatz(number)
except:
    print('Smart. Wanna try that again with a number?')

