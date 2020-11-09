import math

class Calc():
    def __init__(self):
        '''Same as ac()--see below'''
        self.ac()

    def __str__(self):
        '''The string representation of Calc() is the list of calculations.'''
        return self.showcalc()
        
    def __add__(self, other):
        '''Calc1 + Calc2 combines the totals and the lists of caclulations.'''
        self.calculations.extend(other.calculations)
        self.total = other.total
        return self

    def notecalc(self, op, op1, op2):
        '''Add latest calculation to the running list.'''
        calc = ''
        if op == 'log':
            op += op2
        else:
            calc = str(op1) + " "
        calc += str(op) + ' ' + str(op2) + ' = ' + str(self.total)
        self.calculations.append(calc)

    def add(self, op1, op2=None):
        '''Add two numbers. If only one number supplied, add to running total.'''
        if op2 == None:
            op2 = op1
            op1 = self.total
        self.total = op1 + op2
        self.notecalc('+', op1, op2)
        return self.total
        
    def sub(self, op1, op2=None):
        '''Subtract two numbers. If only one number supplied, subtract from
        running total.
        '''

        if op2 == None:
            op2 = op1
            op1 = self.total
        self.total = op1 - op2
        self.notecalc('-', op1, op2)
        return self.total

    def mult(self, op1, op2=None):
        '''Multiply two numbers. If only one number supplied, multiply
        running total.
        '''
        if op2 == None:
            op2 = op1
            op1 = self.total
        self.total = op1 * op2
        self.notecalc('*', op1, op2)
        return self.total

    def pow(self, op1, op2=None):
        '''Raise a number to a power. If no number supplied, raise the
        running total to the power. 
        '''
        if op2 == None:
            op2 = op1
            op1 = self.total
        self.total = math.pow(op1, op2)
        self.notecalc('**', op1, op2)
        return self.total

    def dolog(self, logtype, op1=None):
        '''Take log/log10 of a number. If no number supplied, take log
        of the running total.
        '''
        if op1 == None:
            op1 = self.total
        if logtype == 'log':
            self.total = math.log(op1)
            self.notecalc('log', op1, '')
        else:
            self.total = math.log10(op1)
            self.notecalc('log', op1, '10')
        return self.total
    
    def log(self, op1=None):
        return self.dolog('log', op1)

    def log10(self, op1=None):
        return self.dolog('log10', op1)

    def showcalc(self):
        '''Show current list of calculations.'''
        return '\n'.join(self.calculations)

    def ac(self):
        '''All clear--set total to 0 and erase the list of calculations.'''
        self.calculations = []
        self.total = 0
