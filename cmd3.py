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

# using senario : the user this program only once at the beginning.
# the final return must a list of tuples if in this format [(option, [ars*])]
# and he have to sepecify the number of argument for each option at the beginning.
# return 1, last option if the process wasn't completed sucessful.

# To do cmd3:
# keep the same previous mecanism of getting add analysing the option and thier
# argument. However, this put the in an object, with following implemetation :
#       - The initialisation of the object when is called, should accept the
#       sys.argv directly and provide a method to add them later;
#       - A method for processing the entered parameter and prepare them to be
#       traited (parameters()); Private method DONE
#       - Rather than treating them, I'm going to return then in this format
#       (option, arguments*), and it's up to the user to treat them.
#       - A method for returning the results. DONE
#       - Add a test if sys and collections are imported.

# Hints :
# 1. when a argument is required and option is given instead

import sys
import collections

class readArgs:
    '''Read the parameter form the command line and treate them.'''

    def __init__(self, args):
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
                            raise # 1
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
            # add a function that allows customizing this except
            print('\t{} required {} arugment(s).'.format(ele, rules[ele]))
            print(final_options) #
            exit()

        return final_options

    def getOptions(self):
        return self.finalOptions(self.rules, self.pre_options)

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
    para.addRule('--add', 1)
    para.addRule('--browse')
    print('Rules')
    print(para.rules)
    print('The final result.')
    print(para.getOptions())

    # test the content of the self.pre_options after using action

if __name__ == '__main__':
    main()
