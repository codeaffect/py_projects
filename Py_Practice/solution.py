
class Options:
    def one(self):
        print('one')

    def two(self):
        print('two')

    def if_else(self):
        if_else()


def call_method(o, name):
    return getattr(o, name)()


def if_else():
    n = int(input('Enter Number:'))
    if n % 2 != 0:
        print('Weird')
    else:
        if n >= 2 and n <= 5:
            print('Not Weird')
        elif n >= 6 and n <= 20:
            print('Weird')
        else:
            print('Not Weird')


o = Options()
print('Enter value:')
string = input()

call_method(o, string)
