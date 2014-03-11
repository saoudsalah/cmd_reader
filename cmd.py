# Hints :
# 1. when a argument is required and option is given instead
# 2. add an exception and exit

import sys
import collections

class Duplicated(Exception):
    '''Raising an exception the same option is entered twise.'''

    def __init__(self):
        pass


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


    def addRules(self, multi_rule):
        '''Add multiple rules at the same time.'''

        for opt, arg in multi_rule.items():
            if opt not in self.rules.keys():
                self.rules[opt] = arg
            else:
                # ignore duplicated rules.
                pass


    def finalOptions(self, rules, entiers):
        '''Creating the final output.'''

        final_options = dict()
        temp = list()

        try:
            while len(entiers) > 0:
                ele = entiers.popleft()
                if ele in rules.keys():

                    if ele in final_options.keys():
                        raise Duplicated
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
        except Duplicated:
            print('You entered the same option twise.')
            exit(1)


    def getOptions(self):
        '''Get the final output.'''

        if self.rules == []:
            print('The rules within readArgs aren\'t defined yet.')
            exit(1)
        else:
            return self.finalOptions(self.rules, self.pre_options)


def main():
    '''Main function.'''

    print('The program is lunched.')
    para = readArgs(sys.argv)

    print('Rules')
    para.addRules({'-n': 0, '--help': 0, '--source': 0, '--browse': 0, '-m': 1,
        '-p': 3, '-s': 0})
    print(para.rules)

    print('The final result.')
    print(para.getOptions())


if __name__ == '__main__':
    main()
