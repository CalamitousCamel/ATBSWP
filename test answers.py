spam = ['apples', 'bananas', 'tofu', 'cats']
testlong = ['apples', 'bananas', 'tofu', 'cats', 'snakes', 'rats']
testshort = ['apples', 'bananas']
testone = ['apples', ]


def list2string(arg):
    str_arg = ''
    if len(arg) > 1:
        # for list values except the last 2
        for i in range(len(arg) - 2):
            # appends ', ' to each list item
            str_arg = str_arg + arg[i] + ', '
        # appends arg[-2] then ' and ' then arg[-1]
        str_arg = str_arg + arg[-2] + ' and ' + arg[-1]
    else:
        # exception for single value lists
        str_arg = arg[0]
    print(str_arg)


# from stackoverflow - changes global list values
def commacode(var):
    # mutates last item to 'and var[-1]'
    var[len(var) - 1] = 'and ' + var[len(var) - 1]
    index = 0
    # new_string = var[0]
    new_string = var[index]
    # loop appends ', ' then var[1], iterates +1 index
    while index < len(var) - 1:
        new_string = new_string + ', ' + var[index + 1]
        index = index + 1
        # prints string when index == list length
        if index == len(var) - 1:
            print(new_string)

# list2string called first becasue it doesn't alter global list
# alternate order causes 'and and' in list2string

list2string(spam)
list2string(testlong)
list2string(testshort)
list2string(testone)
print(spam)

print()

commacode(spam)
commacode(testlong)
commacode(testshort)
commacode(testone)
print(spam)
