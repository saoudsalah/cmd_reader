# Cmd_reader : command reader is program that read an interpert the option
# entered with the command and their paramters.

# to do:
#   command [-options] [agrs]
#   Implement a funtion that reads individual entiers, i.e. -p -s -j -k DONE
#   Implement a function that reads individual entiers with their parameters,
#       i.e. -p /path/ -s source DONE.
#   The previous function with add support to grouped paramters -psj , and with
#   The possibility of the later one accepts an argument. DONE.
#   Long parameters support. IMPOSSIBLE WITH THIS IMPLEMETATION

import sys
import collections
import string

# methods to use append() and popleft()

def parameters(args):
    '''Reads arguments'''
# add support for long option --
    queue = collections.deque()
    contin = False

    for ele in args[1:]:
        if contin and not ele[0] == '-':
            # this a argument
            queue.append(ele)

        elif len(ele) >= 2:
            # this an option
            if ele[0] == '-':
                contin = True
                for opt in ele[1:]:
                    queue.append(opt)

    return queue
    #print('\nEnd of loop')
    #print(queue)

def action(queue):
    '''Based on option return respence.'''

    # the validation of entires is done here
    # you must the same number of args as required otherwise a exception'll
    # raised.
    while len(queue) > 0:
        ele = queue.popleft()
        if ele == 'h':
            print('h: help')
        elif ele == 's':
            print('s: source')
        elif ele == 'p':
        # this option accept a parameter
            print('p: path, first arg {}'.format(queue.popleft()))
        elif ele == 't':
            print('t: three args: \n\t first {}'.format(queue.popleft()))
            print('\t second {} \n\t third {}'.format(queue.popleft(),
                queue.popleft()))
        elif ele == '--add':
            print('--add option')

def main():
    '''Main function.'''
    print('The program is lunched.')
    para = parameters(sys.argv)
    action(para)

if __name__ == '__main__':
    main()
