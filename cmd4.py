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
# exit if, the last option wasn't completed sucessfully.

# To do cmd3:
# keep the same previous mecanism of getting add analysing the option and thier
# argument. However, this put the in an object, with following implemetation :
#       - The initialisation of the object when is called, should accept the
#       sys.argv directly and provide a method to add them later;
#       - A method for processing the entered parameter and prepare them to be
#       traited (parameters()); Private method DONE
#       - Rather than treating them, I'm going to return then in this format
#       (option, arguments*), and it's up to the user to treat them. Done
#       - A method for returning the results. DONE
#       - Add a test if sys and collections are imported.

# Todo cmd4:
#       - Return a dict for the final_options, and read the rules from a
#       dictionary.

# Testing:
# a. what if the program is lanched without any argument.
# b. The first arguments are parameters, not option should raise an exception.

# Hints :
# 1. when a argument is required and option is given instead
# 2. add an exception and exit

import sys
import collections

class readArgs:
    '''Read the parameter form the command line and treate them.'''


    def __init__(self, args):
        # sys.argv as argument
       self.args = args
       self.pre_options = self.parameters(self.args)
       self.rules = dict()



    def parameters(self, args):
        '''Reads arguments'''
        queue = collections.deque()
        contin = False

        for ele in args[1:]:
            if contin and not ele[0] == '-':
                # this a argument
                queue.append(ele)

            elif len(ele) >= 2:
                # this an option
                if ele[0] == '-':
                    contin = True # to ajust the starting only
                    if ele[1] == '-':
                        # long options support
                        queue.append(ele)
                    else:
                        for opt in ele[1:]:
                            queue.append('-' + opt)
        return queue



    def addRule(self, opt, arg=0):
        '''Add one rule.'''

        self.rules.append((opt, int(arg)))



    def addRules(self, multi_rule):
        '''Add multiple rules at the same time.'''
        # Rules format [(option, nu_args)*]
        for opt, arg in multi_rule.items():
            if opt not in self.rules.keys():
                self.rules[opt] = arg
            else:
                # ignore duplicated rules.
                pass



    def finalOptions(self, rules, entiers):
        '''Creating the final output.'''

        #rules = dict(rules_tuple)
        final_options = dict()
        temp = list()

        try:
            while len(entiers) > 0:
                ele = entiers.popleft()
                if ele in rules.keys():

                    if ele in final_options.keys():
                        raise
                    else:
                        final_options[ele] = None # option

                    count = rules[ele]
                    while count > 0: # agrs
                        arg = entiers.popleft()
                        if arg[0] == '-':
                            raise ValueError(arg) # 1.
                        else:
                            temp.append(arg)
                            count -= 1

                    final_options[ele] = (tuple(temp))
                    temp = []

                else:
                    # not defined options
                    print('"{}" is not a valid option.'.format(ele))
                    exit(1)

            return final_options

        except IndexError:
            print('\t"{}" require "{}" arugment(s).'.format(ele, rules[ele]))
            exit(1)
        except ValueError as err: # this for non valid argument
            print('"{}" is not an a valid argument.'.format(err))
            exit(1)



    def getOptions(self):
        if self.rules == []:
            print('The rules within readArgs aren\'t defined yet.')
            exit(1)
        else:
            return self.finalOptions(self.rules, self.pre_options)


def main():
    '''Main function.'''
    print('The program is lunched.')
    para = readArgs(sys.argv)
    print('Initial traitement of arguments.')
    #print(para.pre_options)
#
#    para.addRule('-s')
#    para.addRule('-h')
#    para.addRule('-p', 3)
#    para.addRule('-m', 1)
#    para.addRule('--add', 1)
#    para.addRule('--browse')
#    para.addRules((('-n', 0), ('--help', 0), ('--source', 0)))
    para.addRules({'-n': 0, '--help': 0, '--source': 0, '--browse': 0, '-m': 1,
        '-p': 3, '-s': 0})
    print('Rules')
    print(para.rules)
    print('The final result.')
    print(para.getOptions())
    #data = para.getOptions()
    #for opt, args in data:
        #print(opt, '\t', args)

if __name__ == '__main__':
    main()
