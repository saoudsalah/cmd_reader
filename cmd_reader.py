# Cmd_reader : command reader is program that read an interpert the option
# entered with the command and their paramters.

# to do:
#   Implement a funtion that reads individual entiers, i.e. -p -s -j -k
#   Implement a function that reads individual entiers with their parameters,
#       i.e. -p /path/ -s source
#   The previous function with add support to grouped paramters -psj , and with
#   The possibility of the later one accepts an argument.
#   Long parameters support.

import sys
import collections
import string

# methods to use append() and popleft()
def parameters(args):
    queue = collections.deque()

    if len(args) == 1:
        # no args
        print('Program lanched without any argument')
    else:
        for arg in args[1:]:
            queue.append(arg)

    group_start = False
    while len(queue) > 0:
        opt = queue.popleft()
        # this an argument for an option key = val

        if opt[0] == '-' :
            start = True
            opt = opt[1]

        if start:
            #opt = opt[1]

    # simple individual args
            if opt == 'h':
                print('Entered option is h')
            elif opt == 'e':
                print('Entered option is e')
            elif opt == 'm':
                print('Entered option is m')
            elif opt in string.whitespace:
                start = False

            old_opt = opt   # this one to handle option with arguments

# with those the basic rule of - before doesn't work.
    # args with their parameters
        else:
            # this a parameter for an agrument
            # here we need to call the old option

            if old_opt == 'j':
                print('option j with {} parameter'.format(opt))
            elif old_opt == 'p':
                print('option p with {} argument'.format(opt))










    # combined

    # long args

def main():
    '''Main function.'''
    print('The program is lunched.')
    parameters(sys.argv)

if __name__ == '__main__':
    main()
