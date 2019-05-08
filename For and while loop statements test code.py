
mySentence = 'loves the color'

color_list = ['red','blue','green','pink','teal','black']

def color_function(name):
    lst = []
    for i in color_list:
        msg = "{0} {1} {2}".format(name,mySentence,i)
        lst.append(msg)
    return lst

def get_name():
    go = True
    while go:
        name = input('What is your name? ')
        if name == '':
            print('You need to provide you name!')
        elif name == 'Sally':
            print('Sally, you may not use this software.')
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)

get_name()

"""
The way the above code works is:

Notes by Nicson Martinez

1. get_name() gets called,

2. Since the while condition is true, the computer waits for an input from the user after
printing "What is your name? ". The While loop is used in a way catch user input and if it
meets the specific condition in a conditional statement inside of the loop, print specific
message, else exit out of the loop and carry on with the rest of the instructions
(While loop keeps running until go = False).

3. Now that we have the string value that the user entered on the screen stored in variable 'name',
the function color_function(name) gets called and will eventiually store what it returns to a local
variable '1st' (local to get_name()).

4. In color_function(name), an empty list is stored in local variable 'lst' (local to color_function(name)).
the for loop iterates through global variable 'color_list' that contains a list of 6 color elements. So, a
string consisting of 'name' (what the user imputed),'mySentence' (global varable containing a tring), and
'i' which is th current iteration of elements in list 'color_list' get stored in variable 'msg' (which is
a local variable to the for loop). Then lst.append(msg), adds each version of the 'msg' string to a the empty
list 'lst' that we created earlier. So at the end, the list 'lst' will have 6 elements containing 6 different
concatination of strings differenting in color because of the iteration of the 'color_list' using i. Lastly,
it retuns that newly created list containing 6 elements made up of previously concatinated string values.

5. In get_name(), now that we have the returned list in variable 'lst', a for loop is used to iterate through
each of those 6 elements to print each of those elements (a string value made up of previously
concatinated string values) one at atime.

"""
