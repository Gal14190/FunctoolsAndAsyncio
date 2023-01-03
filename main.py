# Afeka college 2022-2023
# Assignment 3
##
# Created at 02/01/2023
# Authors:  Gal Ashkenazi   (315566752)
#           Roy Vaygue      (318860848)
##

## import moduls
import functools
import random

'''
Solusions
'''

'''
        Question 1 Solusion
'''
class Q1:
    def diff_type(self, _list): 
        diff_type_min = 2
        
        return functools.reduce(lambda amount, x: amount + (1 if len(x) >= diff_type_min else 0), list(map(lambda column: set(map(lambda element: type(element), column)) ,_list)), 0)

        '''
        for column in _list
            x add {element for element in column}
            if sizeof x >= 2
                amount + 1

        '''

    def run(self):
        print(self.diff_type([[1,5,3], ['a','v',3], ["sss", 'b'],[], [[3,4,5],['a']], [(4,5,6),[4,5,6]]]))      # 2
        print(self.diff_type([[1,5,3], ['a','v','3'], ["sss", 'b'],[], [[3,4,5],['a']], [(4,5,6),[4,5,6]]]))    # 1
        print(self.diff_type([[1,5,3], ['a','v','3'], ["sss", 'b'],[7,8], [[3,4,5],['a']], [{4,5,6},{4,5,6}]])) # 0
        print(self.diff_type([[1,5,'3'], ['a','v',3], ["sss", 'b'],[], [[3,4,5],['a']], [(4,5,6),[4,5,6]]]))    # 3
'''
        Question 2 Solusion
'''
class Q2:
    def run(self): 
        vlst = ['x' + str(num) for num in range(10)]
        lamdic = {}
        for i,l in enumerate(vlst):
            lamdic[l] = lambda x, i = i: (i + 1) * x    ## complete required

        for v in vlst:
            for i in range(1,len(vlst) + 1):
                print(lamdic[v](i), end=' ')
            print()

'''
        Question 3 Solusion
'''

class a():
    z = 8                          ## complete required
    def __init__(self, y):
        self.y = y                  ## complete required
    def __call__(self, z = z):      ## complete required
        if z > self.y:
            return z - self.y
        else:
            return self.y - z
class b(a):                         ## complete required
    def __call__(self, z = a.z):      ## complete required
        if z > self.y:
            return z - self.y
        else:
            return self.y - z

'''
        Question 4 Solusion
'''
class Q4:
    def sort_list(self, lst):
        for i in range(len(lst)):
            for j in range(len(lst)-1):
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
        return lst

    def run(self):
        print(self.sort_list([9,5,4,1,3]))        # [1, 3, 4, 5, 9]
        print(self.sort_list([7,80,51,20,5]))     # [5, 7, 20, 51, 80]
        print(self.sort_list([33,99,457,100,10])) # [10, 33, 99, 100, 457]

'''
        Question 5 Solusion
'''
class Statistics:
    decorator_counter = 0
    function_counter  = 0
    variables_counter = 0

    def __init__(self, func):
        Statistics.decorator_counter += 1

        self.func = func

    def __call__(self, *args, **kwds):
        Statistics.function_counter  += 1
        Statistics.variables_counter += len(args) + len(kwds)

        self.func(*args, **kwds)

        print(f"Decorator Counter: {Statistics.decorator_counter}\nFunction Counter: {Statistics.function_counter}\nVariables Counter: {Statistics.variables_counter}")

class Q5:
    @Statistics
    def foo():
        print("\nFunction Test 1 Question 5")

    @Statistics
    def bar(a, b, c, x = 0, y = 0, z = 0):
        print("\nFunction Test 2 Question 5")

    def run(self):
        self.foo()
        self.bar(1, 2, 3, x = 2, y = 3, z = 5)
        self.bar(1, 2, 3, x = 2)

'''
        Question 6 Solusion
'''
class Q6:
    def a(self):
        while True:
            # Generate a random number between 1 and 5
            num = random.randint(1, 5)
            # Yield the number to the next coroutine
            yield num

    def b2(self, next_coroutine):
        while True:
            # Get the number from the previous coroutine
            num = (yield)
            # Calculate the result of powering the number by 2
            result = num**2
            # Send the result to the next coroutine
            next_coroutine.send(result)

    def b3(self, next_coroutine):
        while True:
            # Get the number from the previous coroutine
            num = (yield)
            # Calculate the result of powering the number by 3
            result = num**3
            # Send the result to the next coroutine
            next_coroutine.send(result)

    def c(self):
        while True:
            # Get the numbers from the previous coroutines
            num1 = (yield)
            num2 = (yield)
            # Print the sum of the numbers and the original number
            print(f"Sum: {num1 + num2}, Original number: {num1 ** (1/2)}")

    def run(self):
        a = self.a()
        c = self.c()
        b3 = self.b3(c)
        b2 = self.b2(c)

        # forward into the first yield
        a.__next__()
        c.__next__()
        b3.__next__()
        b2.__next__()
    
        # Perform three rounds of the coroutines
        for _ in range(3):
            num = a.__next__()
            b2.send(num)
            b3.send(num)

if __name__ == "__main__":
    ## Question 1
    print("Question 1:")
    q1 = Q1()
    q1.run()

    ## Question 2
    print("\nQuestion 2:")
    q2 = Q2()
    q2.run()

    ## Question 3
    print("\nQuestion 3:")
    print(a(5)(b(6)()))     # 3
    print(a(6)(b(5)(6)))    # 5

    ## Question 4
    print("\nQuestion 4:")
    q4 = Q4()
    q4.run()

    ## Question 5
    print("\nQuestion 5:")
    q5 = Q5()
    q5.run()
    

    ## Question 6
    print("\nQuestion 6:")
    q6 = Q6()
    q6.run()