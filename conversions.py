#!usr/bin/env python3

class Conversion:
    ''' Converts infix expression to postfix and prefix expressions '''
    def __init__(self):
        self.stack = []
        self.precedence = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2}
        self.result = []
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        if self.isEmpty():
            return ''
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack)==0
        
    def isNotGreater(self, op):
        '''
        Checks the precedence of 2 operators
        :param: self: Object
                op: String, operator as a character to push in the stack
        rtype: bool
        '''
        try:
            a = self.precedence[op]
            top = self.precedence[self.peek()]
            return a <= top
        except KeyError:    # if operator not in self.precedence
            return False
    
    def infixToPostfix(self, exp):
        '''
        Convert the given infix expression to postfix expression
        :param: self: Object
                exp: String, expression to be converted
        rtype: String
        '''
        for el in exp:
            if el.isalpha():
                self.result.append(el)
            
            elif el == '(':
                self.push(el)
            
            elif el == ')':
                while self.peek() != '(':
                    self.result.append(self.pop())
                self.pop()
            
            else:
                while (not self.isEmpty() and self.isNotGreater(el)):
                    self.result.append(self.pop())
                self.push(el)
            
        # add the remaining operators to self.result
        while not self.isEmpty():
            self.result.append(self.pop())
        
        return ''.join(self.result)

    def infixToPrefix(self, exp):
        self.stack = []
        self.result = []
        exp = exp[::-1]
        for el in exp:
            if el.isalpha():
                self.result.append(el)
                        
            elif el == ')':
                self.push(el)
            
            elif el == '(':
                while self.peek() != ')':
                    self.result.append(self.pop())
                self.pop()
            
            else:
                while (not self.isEmpty() and self.isNotGreater(el)):
                    self.result.append(self.pop())
                self.push(el)
            
        # # add the remaining operators to self.result
        while not self.isEmpty():
            self.result.append(self.pop())
        
        return ''.join(self.result[::-1])

convert = Conversion()
exp = "(A+B)*C-(D-E)*(F+G)"
print(f'Infix Expression: {exp}')
print(f'Postfix Expression: {convert.infixToPostfix(exp)}')
print(f'Prefix Expression: {convert.infixToPrefix(exp)}')