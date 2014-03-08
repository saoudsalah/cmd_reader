# Cmd_reader : command reader is program that read an interpert the option
# entered with the command and their paramters.

# to do cmd2:
#   command [-options] [agrs]
#   Implement a funtion that reads individual entiers, i.e. -p -s -j -k DONE
#   Implement a function that reads individual entiers with their parameters,
#       i.e. -p /path/ -s source DONE.
#   The previous function with add support to grouped paramters -psj , and with
#   The possibility of the later one accepts an argument. DONE.
#   Long parameters support. Done

# To do cmd3:
# keep the same previous mecanism of getting add analysing the option and thier
# argument. However, this put the in an object, with following implemetation :
#       - The initialisation of the object when is called, should accept the
#       sys.argv directly and provide a method to add them later;
#       - A method for processing the entered parameter and prepare them to be
#       traited (parameters()); Private method DONE
#       - A method for adding cases to action method; Private method
#       - Rather than treating them, I'm going to return then in this format
#       (option, arguments*), and it's up to the user to treat them.
#       - A method for returning the results.

import sys
import collections
import string

# methods to use append() and popleft()

class readArgs:
    '''Read the parameter form the command line and treate them.'''

    def __init__(self, args): # the intialization must be done by passing the
        # sys.argv as argument
       self.args = args
       self.pre_options = self.parameters(self.args)
       self.rules = list()

    def parameters(self, args):
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

    def addRule(self, opt, arg=0): # add one rule at time
        '''Getting the rules of processing input.'''

        self.rules.append((opt, arg))

    def addRules(self, multi_rule):
        '''Add multiple rules at the same time.'''
        # Rules format [(option, nu_args)*]
        # for rule in multi_rule:
            # self.rules.append(rule)
        pass

    def finalOptions(self, rules_tuple, entiers):
        '''Creating the final output.'''
# ['-h', '-s', '-m', '-g', '-a', '-m', '-e', '-p', 'new', '-t', 'first', 'second', '3'])
# [('-s', 0), ('-h', 0), ('-p', 3), ('-m', 1)]

        # transulating the rule to a dictionnary
        rules = dict(rules_tuple)
        final_options = list()
        temp = list()

        try:
            while len(entiers) > 0:
                ele = entiers.popleft()
                if ele in rules.keys():
                    temp.append(ele)
                    count = rules[ele]
                    while count > 0:
                        arg = entiers.popleft()
                        if arg[0] == '-': # an error.
# [bug] : add test before adding to temp if it's an option raise an error
# this kind of input  python cmd3.py -s -h -sh -p first second third -m -s -d
                            print('Raise') #
                            #break # add a raise here
                        else:
                            temp.append(arg)
                            count -= 1

                    final_options.append(tuple(temp))
                    temp = []

                else:
                # ignoring invalid entiers
                    print('\tignore {}'.format(ele)) #
                    pass
        except:
        # [bug] : add a raise to handle the popleft while the entiers is empty and the
        # option still require an argument . FIXED
            #  python cmd3.py -s -h -sh -p first second third -m
            print('\t{} required {} arugment(s).'.format(ele, rules[ele]))
            #final_options.pop() # delete the arg without his parameter
        return final_options

    def getOptions(self):
        return self.finalOptions(self.rules, self.pre_options)

# using senario : the user this program only once at the beginning.
# the final return must a list of tuples if in this format [(option, [ars*])]
# and he have to sepecify the number of argument for each option at the beginning.
# return 1, last option if the process wasn't completed sucessful.

def main():
    '''Main function.'''
    print('The program is lunched.')
    para = readArgs(sys.argv)
    print('Initial traitement of arguments.')
    #print(para.pre_options)

    para.addRule('-s')
    para.addRule('-h')
    para.addRule('-p', 3)
    para.addRule('-m', 1)
    print('Rules')
    print(para.rules)
    print('The final result.')
    print(para.getOptions())

    # test the content of the self.pre_options after using action

if __name__ == '__main__':
    main()
