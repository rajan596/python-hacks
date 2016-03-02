#!/usr/bin/python3

# classes

class calculator:

    def addition(x,y):
        return x+y

    def subtraction(x,y):
        return x-y

    def mult(x,y):
        return mult

    def divide(x,y):
        if y==0:
            print("Error")
            return -1
        else:
            return x/y

print(calculator.addition(2,5))

# class car

class Car:
    name='car-object'
    color='car-color'

    def __init__(self,name,color):
        self.name=name
        self.color=color
    
    def details(self):
        print('name  : ' + self.name)
        print('color : ' + self.color)

if __name__=='__main__':
    c=Car('A','red')
    c.details()
