# Cmd_reader : command reader is program that read an interpert the option
# entered with the command and their paramters.

# to do:
#   command [-options] [agrs]
#   Implement a funtion that reads individual entiers, i.e. -p -s -j -k DONE
#   Implement a function that reads individual entiers with their parameters,
#       i.e. -p /path/ -s source DONE.
#   The previous function with add support to grouped paramters -psj , and with
#   The possibility of the later one accepts an argument. DONE.
#   Long parameters support. Done

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
                if ele[1] == '-':
                    # long args support
                    queue.append(ele)
                else:
                    for opt in ele[1:]:
                        queue.append('-' + opt)

                contin = True # to ajust the starting only


    return queue

def action(queue):
    '''Based on option return respence.'''

    # the validation of entires is done here
    # you must the same number of args as required otherwise a exception'll
    # raised. You should popleft as much as arguments you need.
    while len(queue) > 0:
        # [Bug] : add an other check when argument is not entred not pop the next
        # option but raise an error
        # Create a list of different options and each poped item should be
        # containeted within this list.
        try:
            ele = queue.popleft()
            if ele == '-h':
                print('h: help')
            elif ele == '-s':
                print('s: source')
            elif ele == '-p':
            # this option accept a parameter
                print('p: path, first arg {}'.format(queue.popleft()))
            elif ele == '-t':
                print('t: three args: \n\t first {}'.format(queue.popleft()))
                print('\t second {} \n\t third {}'.format(queue.popleft(),
                    queue.popleft()))
            elif ele == '--add':
                print('--add option, with this arg {}'.format(queue.popleft()))
            elif ele == '--browse':
                print('--browse option')
            else: # just ignore invalid entries
                pass
        except:
            print('Not enough arguments, to use this command {}'.format(ele))
            break # when an error happened he'll exit


def main():
    '''Main function.'''
    print('The program is lunched.')
    para = parameters(sys.argv)
    action(para)

if __name__ == '__main__':
    main()
