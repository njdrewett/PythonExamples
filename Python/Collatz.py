#Collatz

def collatz(number):
    if number % 2 == 0:
        print (str(number) +' // 2')
        return number // 2
    else:
        print('3 * ' + str(number) + ' + 1')
        return 3 * number + 1

def loopCallatz(number):
    while number > 1:
        response = collatz(number)
        print('Response = ' + str(response))
        number = response

def requestForCollatz():
    print('Enter number:')
    try:
        number = int(input())
        print('Using number ' + str(number))
        loopCallatz(number)
    except ValueError:
        print('Input is not a number')


try :
    while True:
        requestForCollatz()
except KeyboardInterrupt:
    sys.exit()


