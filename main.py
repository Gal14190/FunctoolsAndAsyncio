# Afeka college 2022-2023
# Assignment 3
##
# Created at 15/12/2022
# Authors:  Gal Ashkenazi   (315566752)
##

## import moduls
import functools

'''
Solusions & UnitTests
'''

class Q1():
    def run(self, _list): 
        diff_type_amount = 2
        return functools.reduce(lambda amount, x: amount + (1 if len(x) >= diff_type_amount else 0),list(map(lambda column: set(map(lambda element: type(element), column)) ,_list)), 0)

class Q2():
    def run(self): 
        vlst = ['x'+str(num) for num in range(10)]
        lamdic = {}
        for i,l in enumerate(vlst):
            pass                    ## TODO: complete required

        for v in vlst:
            for i in range(1,len(vlst)+1):
                print(lamdic[v](i),end=' ')
            print()


        
if __name__ == "__main__":
    print("Question 1:")
    q1 = Q1()
    print(q1.run([[1,5,3], ['a','v',3], ["sss", 'b'],[], [[3,4,5],['a']], [(4,5,6),[4,5,6]]]))      # 2
    print(q1.run([[1,5,3], ['a','v','3'], ["sss", 'b'],[], [[3,4,5],['a']], [(4,5,6),[4,5,6]]]))    # 1
    print(q1.run([[1,5,3], ['a','v','3'], ["sss", 'b'],[7,8], [[3,4,5],['a']], [{4,5,6},{4,5,6}]])) # 0
    print(q1.run([[1,5,'3'], ['a','v',3], ["sss", 'b'],[], [[3,4,5],['a']], [(4,5,6),[4,5,6]]]))    # 3

    print("Question 2:")
    q2 = Q2()
    q2.run()