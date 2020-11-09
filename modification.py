class Modification(): 
    """ Lab: __getattr and __setattr
    create an object which holds a value and has a "modification" counter which keeps track of how many times the object has been modified
    for example, the value could be in an attribute called value, so you'll want to notice when you make changes to value and increment the counter
    if you allow modifications to other attributes, you won't increment the counter
    consider rejecting attempts to modify the counter attribute directly
    you will need to use super(), Python's way to call a method in the parent (superclass) in order to actually modify the attribute...why?
    """

    def __init__(self, value, frog):
        self.value = value       
        self.frog = frog

    def __setattr__(self, name, value):
        if name is "value":
            self.__dict__[name] = value
            if 'modification' in self.__dict__.keys():
                super().__setattr__('modification',self.modification + 1)
            else: 
                super().__setattr__('modification',0)
        elif name is 'modification':
            print("No way!")
        else:
            self.__dict__[name] = value


m1 = Modification('Ernie', 'Kermit')
print('ans:',m1.value, m1.modification, m1.frog)
m1.value = 'Bert'
print('ans:',m1.value, m1.modification, m1.frog)
m1.modification = 75
print('ans:',m1.value, m1.modification, m1.frog)
m1.value = 'Big Bird'
m1.frog = "bullfrog"
print('ans: ',m1.value, m1.modification, m1.frog)
