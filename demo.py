print("Hello World")
x = 2
y = 3
print("----------------------variable ----------------------")
print(x)
print(y)
print(id(x))
print(id(y))
z = 2
print(id(2))
print(id(z))
z = "Lalchan"
print(z,id(z))
z = 2;
print(z,id(z))
print("-------------------List--------------------------------")
lis = [12,23,34,8]
print(type(lis),lis)
print(len(lis))
lis.sort()
print(lis)
print(lis[:-1])
lis.append("Lalchan")
lis.insert(0,233)
print(lis)
print(lis.index(233))
temp_lis = ["Golu","Paji","Patel"]
print(temp_lis)
lis.extend(temp_lis)
print(lis)
lis.append(233)
print(lis.count(233))
cop = []
cop = lis
print(cop)
cop.clear()
print(cop)
mylis = list((12,"Lalchan",2021))
print(mylis)

print("---------------------Tuple-----------------------")
tup = (12,23,45,"lolu")
print(type(tup),tup)
print(tup.count(12))
print(tup.index("lolu"))
print(tup[3])
tup_pack = 12,34,56,78
print(type(tup_pack),tup_pack)
print("----------------------set-------------------------")
se = {2,34,32,12,34,90}
print(se)
print(len(se))
se.add(222)
print(se)
print("--------------------------Dictionary-----------------------")
d ={"Maa":"Sony","Patel":"Samsung","Golu":"Redmi","Nanhe":"Redmi"}
print(d)
print(d.keys())
print(d.values())
print(d["Golu"])
key = [1,2,3]
val = [4,5,6];
dc = zip(key,val)
# print(type(*dc))

print("---------------------------------math function----------------------")
'''
import math

print(math.sqrt(34))
print(math.floor(math.sqrt(34)))
print(math.ceil(math.sqrt(34)))
print("------------------------operators------------------------------------")
print(2+3)
print(2*3)
print(45-43)
print(34/3)
print(34//3)
print(3**3)
x = 34
x += 3
y = 32
y -= 21
print(x, y)
print(x<y)
print(x>=y)
print(x==y)
print(~12)

print("-----------------logical operator----------------------------")

x = 5
y = 7
print(x<7 and y<5)
print(x<7 or y<3)
print(x == 56)
print(x != y)

print("-------------swap 2 variables ----------------------------")

a = 23
b = 45
a = a+b
b = a-b
a = a-b
print(a,b)
a = a^b
b = a^b
a = a^b
print(a,b)


print("------------------------number systems-------------------------------")

print(bin(25))
print(0b01101)
print(oct(25))
print(0o31)
print(hex(25))
print(0x19)

print("--------------------User input-----------------------------")
x = input("enter 1st num")
y = input("enter 2nd num")
print(x+y)
a = int(x)
b = int(y)
print(a+b)
num1 = int(input("enter 1st number"))
num2 = int(input("enter 2nd number"))
print(num1/num2)
import sys
# x = int(sys.argv[1])
# y = int(sys.argv[2])
# print(x+y)

print("----------------------If elif else----------------------------")

# Q1. Write a program to take a number input from user and check whether it is odd or even. If it is 0 print Zero.

num = int(input("enter a number"))
if num == 0:
    print("Zero")
elif num%2 == 0:
    print("Even number")
else:
    print("Odd number")

print("-----------------------------While loop-------------------------")


# Q1. print all even number from 0 to 50.
i = 0
while i <= 50:
    if i == 0 or i%2 == 0:
        print(i, end = " ")
    i += 1
print()
print("-----------------------------for loop-------------------------")

#Q1. Write a python program to find the number in range 1 to 50 which is divisible by either 3 or 5 but not divisible by both.

for i in range(1,51):
    if i%3 == 0 and i%5 == 0:
        continue
    elif i%3 == 0 or i%5 == 0:
        print(i, end = " ")
print()

print("-----------------------------for else loop-------------------------")

# Q1. Write a python program.take two input from user. print all  prime numbers between range. if no such numbers are there
# print "Not found".

l = int(input("entert left limit"))
r = int(input("enter right limit"))
for i in range(l,r+1):
    for j in range(2,math.floor(math.sqrt(i))+1):
        if i%j == 0:
            break
    else:
        print(i,end = " ")


print("-----------------------------array-------------------------")
from array import *
arr = array('i',{1,2,3,4,5})
print(arr)
for e in arr:
    print(e,end= " ")
print()
for i in range(len(arr)):
    print(arr[i],end = " ")
print()
arr = sorted(arr)
print(arr)

newarr = array('i',{})
n = int(input("enter size of array"))
print("enter ",n," elements")
for i in range(n):
    x = int(input())
    newarr.append(x)
print(newarr)

print("-----------------------------numpy-------------------------")

from numpy import *

arr = array([1,2,3,4,5])
print(arr)
a = linspace(1,15)
print(a)
b = logspace(1,40,10)
print(b)
c = arange(2,10,2)
print(c)
d = ones(10,int)
print(d)
e = zeros(5)
print(e)


# Q write a pytho program take array input from user and search for an element given by user.
from array import *
ar = array('i',{})
n = int(input("enter size of array"))
for i in range(n):
    print("enter ", i+1,"th element")
    x = int(input())
    ar.append(x)
print(ar)
key = int(input("enter element to be searched: "))
for i in range(n):
    if key == ar[i]:
        print(i)
        break
else:
    print("not found")

print("-----------------------------different operations on array -------------------------")

from numpy import *
arr = array([2,6,5,4,3])
print(arr)
# copying array
arr_c = arr    # shallow copy
print(arr_c)
print(id(arr))
print(id(arr_c))
arr[3] = 0
print(arr_c)

arr2 = arr.view()   # different address but still shallow copy
print(id(arr))
print(id(arr2))
print(arr2)

print(min(arr))
print(max(arr))
arr3 = arr + arr_c
print(arr3)
print(sum(arr))
print(sin(arr))
print(cos(arr))
print(log(arr))

print("-----------------------------matrix -------------------------")
from numpy import *
arr = array([1,2,3,4,5,6,7,8,9])
arr2 = arr.reshape(3,3)
print(arr2)
m = mat(arr2)
print(type(m))
print(type(arr2))
print(m)
m1 = mat("2 5 8 ; 3 5 6 ; 1 2 3")
print(m1,type(m1))
print(m1+m)
print(m1*m)
print(diag(m1))

print(m.shape)

print("-----------------------------matrix multiplication -------------------------")

mat1 = array([[1,2,3],[4,5,6],[7,8,9]])
mat2 = array([[2,3,4],[9,8,7],[3,4,5]])
print(mat1)
print(mat2)
print(mat1+mat2)
print(mat1*mat2)
print(mat1.dot(mat2))
print(diag(mat1))

res = zeros((3,3),int)
for i in range(mat1.shape[0]):
    for j in range(mat1.shape[1]):
        for k in range(3):
            res[i][j] += mat1[i][k]*mat2[k][j]
print(res)

print("-----------------------------functions -------------------------")

def add(a,b):           #formal arguement
    print(a,b)
    print(a+b)
add(3,4)            #actual arguement
x = 5
y = 7
add(x,y)        #positional arguement
add(b=8,a=9)    # keyword arguement

def person(name, age = 18):     #default arguement
    print(" name :", name)
    print(" age :", age)
person("lalchan")
person("golu", 23)

def sum(a,*b):      #variable length arguement
    print(a,b)
    res = 0
    for i in b:
        res += i
    print(res)

sum(2,9,77,54,98)

def data(name,**details):       # variable length keyword arguement
    print(name)
    for i,j, in details.items():
        print(i,j)
data("lalchan",city = "patna", age = 20)

print("-----------------------------Global vs local -------------------------")

a = 10
name = "lalchan"
def fun():
    global a
    x = globals()
    name = "golu"
    print(x['name'],name)
    print(id(a))
    print(a)
    a = 15;
    print(a)
    print(id(a))

fun()

print("-----------------------------passing list to a function -------------------------")
def count(lst):
    even = 0
    odd = 0
    for each in lst:
        if each %2 == 0:
            even += 1;
        else:
            odd += 1
    return odd,even
lst = [1,2,3,4,5,6,7,8,9,10]

odd,even = count(lst)
print(odd,even)

print("-----------------------------fibonaci sequence -------------------------")
# Q print n fibonaci number from 0
def fib(n):
    if n<0:
        print("invalid input")
        return
    a = 0
    b = 1
    if n == 1:
        print(a)
        return
    if n == 2:
        print(a,b)
        return
    print(a,b,end = " ")
    for i in range(2,n):
        c = a+b
        a = b
        b = c
        print(c,end=" ")

fib(10)
print()
print("-----------------------------factorial using recurssion -------------------------")

def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1);

print(fact(10))
print("-----------------------------lambdA function -------------------------")

x = lambda a: a*a
print(x(21))
print("-----------------------------filter, map, reduce -------------------------")


lst = [2,3,4,5,6,7,8,9,10,32,45,222,121,23]
def odd(n):
    return n%2 == 1
odd_without = list(filter(odd,lst))
print("odd in map without lambda : ",odd_without)
odd_with = list(filter(lambda x : x%2 == 1, lst))
print("odd in map with lambda : ",odd_with)

def update(n):
    return n+2
update_lst = list(map(update,lst))
print(update_lst)

update_lst_lambda = list(map(lambda x : x+2, lst))
print(update_lst_lambda)


def get_sum(a,b):
    return a+b
from functools import  reduce
sum = reduce(get_sum,lst)
print(sum)
sum_with_lambda = reduce(lambda x,y : x+y, lst)
print(sum_with_lambda)
'''
print("-----------------------------decoraters -------------------------")

def div(a,b):
    return a/b
def smart_div(fun):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return fun(a,b)
    return inner
div = smart_div(div)
print(div(2,4))
print(div(10,3))
print(div(3,10))

print("-----------------------------modules -------------------------")
import module as m
m.add(3,4)
m.sub(45,32)
m.mul(2,55)
m.div(3,4)

print(__name__)

print("-----------------------------oops (class,objects,variable,method)-------------------------")

class student:

    total_student = 0    #class variaBLE
    def __init__(self,name,rollno):
        self.name = name            # instance variable
        self.rollno = rollno
        student.total_student +=1
    def show(self):                 #instance method
        print("name :",self.name)
        print("roll no. :",self.rollno)
        print("**********")
    @classmethod # class method
    def showstudent(cls):
        print("total no. of student = ",student.total_student)


s1 = student("lalchan",101)
s2 = student("golu",102)
s1.show()
student.showstudent()

print("-----------------------------oops (inner class)-------------------------")
class employee:
    def __init__(self,ename,eid,lap):
        self.name = ename
        self.id = eid
        self.ram = lap.ram
        self.cpu = lap.cpu
    # def __init__(self,ename,eid):
    #     self.name = ename
    #     self.id = eid
    def show(self):
        print(self.name,self.id,self.ram,self.cpu)
    class laptop:
        def __init__(self,ram,cpu):
            print("inner init")
            self.ram = ram
            self.cpu = cpu


lap1 = employee.laptop(8,"i7")
e1 = employee("lalchan","c89",lap1)
e1.show()
e2 = employee("golu",154,lap1)
e2.show()

print("-----------------------------oops (inheritance)-------------------------")

class A:
    def __init__(self):
        print("A init")
    def feature1(self):
        print("feature1 working")

class B(A):
    def __init__(self):
        print("B init")
    def feature2(self):
        print("feature2 working")

class C(A):
    def __init__(self):
        print("C init")
    def feature3(self):
        print("feature3 working")

objA = A()
objB = B()
objB.feature1()
objB.feature2()
objC = C()
# objC.feature2()
objC.feature1()
objC.feature3()