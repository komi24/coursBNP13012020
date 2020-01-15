#!/usr/bin/env python
# coding: utf-8

# In[4]:


my_list = [] # create an empty list

len(my_list) # size of your list

my_list.extend([4,2,6,8]) # add 4, 2, 6 and 8 in your list

len(my_list)

my_list[0] = 12 #  change first element

my_list


# In[5]:


for element in my_list:
    print(element)


# In[13]:


age_list = [42,38,14,25]
name_list = ["Martin", "Dorianne", "Justine", "Pierre"]

# for i in range(len(age_list)):
#     print(f"{name_list[i]} is {age_list[i]} y.o.")

# for i, age in enumerate(age_list):
#     print(f"{name_list[i]} is {age} y.o.")

for age, name in zip(age_list, name_list):
    print(f"{name} is {age} y.o.")
    
# from itertools import product

# # Get every possibilty between the two lists
# for age, name in product(age_list, name_list):
#     print(f"{name} is {age} y.o.")


# In[15]:


age = 22

if age > 18:
    print("majeur")
elif age < 24:
    print("mineur")
# else:
#     print("passe ton bac")


# In[16]:


if age > 18:
    print("majeur")
if age < 24:
    print("mineur")


# In[19]:


if age == 18:
    print("You are 18")
    
if age != 18:
    print("You are not 18")
    
nationality = "French"
if age == 18 and nationality == "French":
    print("You are 18 and french")
    
if age == 18 or nationality == "French":
    print("You are 18 or french")


# ### Fizz buzz
# 
# For every number form 0 to 100 print :
# 
# * fizz if it's divisible by 3
# * buzz if it's divisible by 5
# * bazz if it's divisble by 3 and 5
# * else print the number
# 
# 
# We'll get 
# 
# bazz
# 
# 1
# 
# 2
# 
# fizz
# 
# 4
# 
# buzz
# 
# ...

# In[18]:


# check if 8 is divisible by 4
9 % 4 == 0 # check if it's equal to zero


# In[24]:


for i in range(100):
    if i % 15 == 0:
        print("bazz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)


# ### Bubble sort
# 
# Sort elements in a list by comparing each element to the following one and changing their order if needed.
# 

# In[31]:


my_list = [4,3,9,4,1,7,0]

for i in range(len(my_list)-1):
    if my_list[i] > my_list[i+1]:
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print(my_list)


# In[ ]:


a = 2
b = 4

a, b = 2, 4


# In[32]:


name = input("What's your name ?")


# In[33]:


print(name)


# In[37]:


age = int(input("How old are you ?"))


# In[38]:


print(age + 1)


# ### Dichotomy search
# 
# * The computer generates a random number between 0 and 100
# * Then the user make a proposition to guess the number
# * If the proposition is too big, the computer prints "too big" and the
#    user can make another propsition
# * If the propostion is too small the computer prints "too small" and the
#    user can make another propsition
# * Else the computer print "You won"
# 

# In[39]:


i = 0
while i < 10:
    i += 1
    print(i)
    if i > 5:
        break
        


# In[41]:


i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i) # we won't execute this if i == 5
        


# ### Dichotomy search
# 
# * The computer generates a random number between 0 and 100
# * Then the user make a proposition to guess the number
# * If the proposition is too big, the computer prints "too big" and the
#    user can make another propsition
# * If the propostion is too small the computer prints "too small" and the
#    user can make another propsition
# * Else the computer print "You won"
# 

# In[51]:


from random import randint

number_to_guess = randint(0, 100)

proposition = int(input("Guess the number"))

while proposition != number_to_guess:
    if proposition > number_to_guess:
        print("Too big")
    elif proposition < number_to_guess:
        print("Too small")
    proposition = int(input("Guess the number"))

print("You won")


# ### Functions
# 

# In[52]:


def addition(a, b):
    return a + b

resultat = addition(2, 4)
print(resultat)


# In[54]:


def exchange_first_and_second(list_input):
    list_input[0], list_input[1] = list_input[1], list_input[0]
    
my_list = [1,5,3,6]
exchange_first_and_second(my_list)
print(my_list)


# In[57]:


def say_hello():
    print("hello world")
    
say_hello # nothing happen with no parenthesis
say_hello() # we need parenthesis to call the function


# In[70]:


def greetings(name, age=32, city="Paris"):
    print(f"Hello {name}. You are {age} y.o. And you live in {city}")

def greetings_with_no_default_param(name, age):
    print(f"Hello {name}. You are {age} y.o.")


# In[72]:


greetings("Justine")
greetings("Justine", 42)
greetings("Justine", "Paris") # Paris is going to be the age parameter here
greetings("Oliver", city="London")

# greetings_with_no_default_param("Justine") # Does not work because we need two params


# In[73]:


def mean(list_input, number_of_elements=None):
    """
        returns the average of elements in the list
        if number_of_elements is not None,
        returns the average of the n-th first elements
        
        :Example:
        >>> mean([2,4,5], 2)
        3
    """


# In[90]:


def merge(array1, array2):
    """
        returns a sorted array containing
        all elements from array1 and array2
        :example:
        >>> merge([2,3,5], [0,7,8])
        [0,2,3,5,7,8]
    """
    i = 0
    j = 0
    result = []
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1
    # add remaining elements from array1 or array2
    result.extend(array1[i:])
    result.extend(array2[j:])
    return result

merge([2,4,7], [5,6,9])
# def merge_sort(array):
#     if len(array) ...:
#         ...
#     else:
#         return merge(
#             merge_sort(array[...]), # first half 
#             merge_sort(array[...]), # second half
#         )


# In[86]:


my_list= [1]
my_list.append(2)


# In[87]:


my_list


# In[91]:


def create_users(username_list, userage_list):
    """
    returns an array of dictionary-like users  
    :Example:
    >>> create_users(["Martin",...], [22,...])
    [{name: Martin, age: 22}, ...]
    """
    return 


# In[99]:


list_number = [4,5,6,12] # list of numbers

list_boolean = [True, False, True] # List of boolean
# list_boolean.append(2)

list_dictionary = [{"name": "Justine"}, {"name": "Helene"}]
list_dictionary.append({"name": "Roger"})
print(list_dictionary)

number = 4
number.append(4)


# In[108]:


list_of_list = [[0], [4]]
list_of_list[1][0]


# In[114]:


def create_users(username_list, userage_list):
    """
    returns an array of dictionary-like users  
    :Example:
    >>> create_users(["Martin",...], [22,...])
    [{name: Martin, age: 22}, ...]
    """
    result = []
    for name, age in zip(username_list, userage_list):
        result.append({"name": name, "age": age})
    return result

users = create_users(["George", "Washington", "Bush"], [42,36,28])


# In[115]:


dico = {"age": 42}
b = dico
b["age"] = 28

print(dico)


# In[117]:


# users[0][age] won't work because age is not a variable
users[0]["age"]


# In[118]:


def filter_threshold(user_list, threshold):
    """
    Get all users with age above this threshold
    """
    result = []
    for user in user_list:
        if user["age"] > threshold:
            result.append(user)
    return result

filter_threshold(users, 30)


# In[122]:


# Works but not good
name = "Gregoire"

def say_hello():
    print(f"Hello {name}")
    
say_hello()


# In[123]:


# Works but not good
def say_hello():
    print(f"Hello {name2}")

name2 = "Boby"

say_hello()


# In[126]:


# Works 
def say_hello(name):
    print(f"Hello {name}")

name= "Alain"
name2 = "Boby"

say_hello(name2)


# In[127]:


# Works but not good

name = "Alain"

def say_hello():
    name = "George"
    print(f"Hello {name}")

name = "Boby"

say_hello()
print(name)


# In[128]:


# Not working

name = "Alain"

def say_hello():
    print(f"Hello {name}")
    name = "George"

name = "Boby"

say_hello()
print(name)


# In[129]:


# global

name = "Alain"

def say_hello():
    global name
    print(f"Hello {name}")
    name = "George"

name = "Boby"

say_hello()
print(name)


# In[132]:


# return

name = "Alain"

def say_hello():
    name2 = "George"
    print(f"Hello {name2}")
    return name2

name = "Boby"

name = say_hello()
print(name)


# In[133]:


# Prints "Hello Mathieu" not "Hello Eloise"
def say_hello(name):
    print(f"hello {name}")
    
name = "Eloise"
name2 = "Mathieu"

say_hello(name2)


# In[ ]:


def filter_threshold(user_list, filter_fct):
    """
    Get all users with age above this threshold
    """
    result = []
    for user in user_list:
        if filter_fct(user):
            result.append(user)
    return result

def my_filter(...):
    """
    Filter people with names larger than 4 characters and older than 18
    """
    ...
    
filter_threshold(users, my_filter) 


# In[160]:


import pandas as pd


df = pd.read_csv("../train.csv")

df["Agex2"] = df.Age.map(lambda age: age * 2)
df["State"] = df.Age.map(lambda age: "mineur" if age < 18 else "majeur")
df


# In[158]:


def my_function(name, is_underage, age=24, city="Paris"):
    print(f"Hello {name} you are {age} y.o.")
    if is_underage(age):
        print("mineur")
    else:
        print("majeur")

def is_less_than_18(age):
    return age < 18

def is_less_than_21(age):
    return age < 21

def is_underage(age, city):
    if city == "LA":
        return is_less_than_21(age)
    else:
        return is_less_than_18(age)
    
my_function("Martin", lambda age: age > 18)
# my_function("Noelia", is_underage, 32)
# my_function("John", is_underage, city="Teheran")


# In[147]:


my_list = []
for i in range(10):
    my_list.append(i * 2)
    
my_list = [i*2 for i in range(10)] # comprehensive list


# In[150]:


def is_less_than_18(age):
    if age < 18:
        return "mineur"
    else:
        return "majeur"
my_list = [ is_less_than_18(user["age"]) for user in users ]
my_list


# In[151]:


my_list = [ ("majeur" if user["age"] > 18 else "mineur") for user in users ]
my_list


# In[152]:


state = "majeur" if users["age"] > 18 else "mineur"
print(state)


# In[156]:


[ user["name"] for user in users]


# In[ ]:


# comprehensive list
my_list = [ user["name"] for user in users]

# conditional affectation
state = "majeur" if users["age"] > 18 else "mineur"

# lambda function
func = lambda x: x * 2


# ### Next things to come
# 
# * Python environement
# * Object Oriented Programing
# * Tests

# In[168]:


# Install modules in the command line interface
pip install --user virtualenv
# Create a list of installed external modules
pip freeze > requirements.txt
# Install a list of external modules
pip install –r requirements.txt
# Create a virtual env
python -m venv .env
# Activate / Deactivate environment
source .env/bin/activate
deactivate

pip install --user selenium


# In[169]:


from MyPackage.module1 import say_hello

say_hello()


# In[185]:


class Person:
    def __init__(self, prenom, location="Paris"):
        self.first_name = prenom
        self.last_name = "Gregovia"
        self.location = location
    
    def say_hi(self):
        print(f"Hello my name is {self.first_name}")

    def greetings(self, other):
        """
        take one parameter : other
        prints Hello {the other's firstname}, my name is {my firstname}
        """
        assert type(other) is Person, "other should be a person"
        print(f"Hello {other.first_name} my name is {self.first_name}")
        
    def __repr__(self):
        return self.first_name
    
one_person = Person("Gloria")
second_person = Person("Melina", "Lyon")

one_person.say_hi()
second_person.say_hi()
one_person.greetings(second_person)
print(one_person.first_name)
print(second_person.first_name)
print(second_person.location)

print(one_person)


# In[189]:


import numpy as np
from functools import total_ordering

@total_ordering
class Car:
    """
    - brand: str
    - speed: float (default 0)
    - position: (default [0, 0])
    - direction: (default [1, 0])
    
    methods:
    - accelerate: add one to the speed
    - stop: speed = 0
    - run: position += direction -> we will need numpy for this part
    - turn: direction turn 90° clockwise -> we will need numpy
    """
    def __init__(self, brand, speed=0, position=np.array([0,0]), direction=np.array([1,0])):
        self.brand = brand
        self.speed = speed
        self.position = position
        self.direction = direction
    def accelerate(self):
        self.speed += 1
    def stop(self):
        self.speed = 0
    def run(self):
        self.position += self.direction
    def turn(self):
        self.direction = np.array([[0,1],[-1,0]]).dot(self.direction)
    def __repr__(self):
        return str(self.position)
    def __lt__(self, other):
        return self.speed < other.speed
    def __eq__(self, other):
        return self.speed == other.speed

car1 = Car("Maybach")
for i in range(10):
    car1.run()
    if i % 3 == 0:
        car1.turn()
    print(car1)


# In[194]:



def uppercase(func):
    print("start anotation")
    def new_function(name):
        new_name = name.upper()
        return func(new_name)
    return new_function

@uppercase
def say_hi(name):
    print(f"hello {name}")
    
say_hi("Luc")
say_hi("James")
say_hi("John")
say_hi("Bobby")


# In[206]:


class Person:
    def __init__(self, prenom, location="Paris"):
        self.first_name = prenom
        self.last_name = "Gregovia"
        self.location = location
        # add an account for each Person
        self.account = Account()
        
    def __repr__(self):
        return self.first_name
    
class Account:
    """
    - balance (default 1000)
    
    methods
    - withdraw(amount) withdraw this amount to balance
    - deposit(amount) add this amount to balance
    """
    nb_of_accounts = 0
    def __init__(self, balance=1000):
        self.id = Account.nb_of_accounts
        self.__balance = balance
        Account.nb_of_accounts += 1
        
    def balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        assert condition, "Not enough money on the account"
        self.__balance -= amount
    
    def deposit(self, amount):
        self.__balance += amount
        
    def __repr__(self):
        return f"id: {self.id} - balance : {self.__balance}"

someone = Person("Elisa")
someone_else = Person("Gaby")
print(someone.account)
print(someone_else.account)

# someone.account.balance = 50
# someone.account.__balance -= 50


# In[212]:


import unittest

class AccountTestCase(unittest.TestCase):
    def setUp(self):
        self.account = Account(2000)
    def testBalanceIsOk(self):
        self.assertEqual(self.account.balance(), 2000)
    def testBasicWithdrawal(self):
        self.account.withdraw(200)
        self.assertEqual(self.account.balance(), 1800)
    def testWithdrawTooMuch(self):
        with self.assertRaises(AssertionError):
            self.account.withdraw(1000000)

unittest.main(argv=['first-arg-is-ignored'], exit=False)


# In[216]:


with open("list_users.txt", "a") as f:
    f.write("bonjour")


# In[218]:


with open("list_users.txt", "r") as f:
    print(f.read())


# In[223]:


import pandas as pd

df = pd.read_csv("../train.csv")
df


# In[228]:


import re

text = "Bonjour my number is 0637618981"

re.findall(".+", text) # any character at least one time
re.findall(".*", text) # any character from zero to any time
re.findall("[0-9]{10}", text) # 10 numbers

re.sub("[0-9]{10}", "[anonymous_number]", text) # 10 numbers


# In[ ]:


https://github.com/komi24/coursBNP13012020

