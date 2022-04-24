""" This is an calculator example we are going to  see
"""
class operators:
    def __init__(self):
        pass
    def plus(self,a,b):
        """ this function makes addition of a and b"""
        return a+b
    def minus(self,a,b):
        return a-b
    def times(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b

def main():
    """this is our main aplication function"""
    runtimee =True
    print("~~~~~~~~~~~~~WELCOME~~~~~~~~~~~~~")
    result = 0
    while runtimee:
        """we make an infinite loop so our user can use it again and again until if they want to exit"""
        x = input("select your operation from these options(+,-,*,/)\nand do the job or write exit to go out--> ")
        if x=="exit":
            runtimee=False
            print("~~~~~~~~~~~~~GOODBYE~~~~~~~~~~~~~")
        elif x=="+":
            a = input("write your first value and press enter--> ") # input is a built-in function in python it takes a value in string format so to be able to do our operation we changed our value into float
            b = input("write your second value and press enter--> ")
            a = float(a)
            b = float(b)
            result = operators().plus(a,b) # we called our operation class' function
            print("= ",result)
        elif x=="-":
            a = input("write your first value and press enter--> ") # input is a built-in function in python it takes a value in string format so to be able to do our operation we changed our value into float
            b = input("write your second value and press enter--> ")
            a = float(a)
            b = float(b)
            result = operators().minus(a,b) # we called our operation class' function
            print("= ",result)
        elif x=="*":
            a = input("write your first value and press enter--> ") # input is a built-in function in python it takes a value in string format so to be able to do our operation we changed our value into float
            b = input("write your second value and press enter--> ")
            a = float(a)
            b = float(b)
            result = operators().times(a,b) # we called our operation class' function
            print("= ",result)
        elif x=="/":
            a = input("write your first value and press enter--> ") # input is a built-in function in python it takes a value in string format so to be able to do our operation we changed our value into float
            b = input("write your second value and press enter--> ")
            a = float(a)
            b = float(b)
            result = operators().divide(a,b) # we called our operation class' function
            print("= ",result)


        else:
            print("you did not choose an operation or \nwrote exit please try to write something from options")

        
main() # we call
