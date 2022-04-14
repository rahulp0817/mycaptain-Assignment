#Implement methods of list data structure. Assignment - 1

1.append()

list = [1, 2, 4, "Mango", "Apple"]
list.append("Orange")
print(list)

OUTPUT = [1, 2, 4, "Mango", "Apple", "Orange"]

2.clear()

list = [1, 2, 4, "Mango", "Apple"]
list.clear()
print(list)

OUTPUT = []

3.pop()

list = [1, 2, 4, "Mango", "Apple"]
list.pop()
print(list)

OUTPUT = [1, 2, 4, "Mango"]

4.insert()

list = [1, 2, 4, "Mango", "Apple"]
list.insert(3, 21)
print(list)

OUTPUT = [1, 2, 4, 21, "Mango", "Apple"]

5.remove()

list = [1, 2, 4, "Mango", "Apple"]
list.remove("Mango")
print(list)

OUTPUT = [1, 2, 4, 21, "Apple"]

6.count()   (....)

list = [1, 2, 4, "Mango", "Apple"]
print(list.count("Mango"))

OUTPUT = 1

7.sort()

list = [1, 6, 4]
list.sort()
print(list)

OUTPUT = [1, 2, 6]

8.copy()    (.....)

list = [1, 2, 4, "Mango", "Apple"]
print(list.count("Mango"))

OUTPUT = [1, 2, 4, "Mango", "Apple"]

9.extend()

list = [1, 2, 4, "Mango", "Apple"]
cars = ['Ford', 'BMW', 'Volvo']
list.extend(cars)

OUTPUT = [1, 2, 4, "Mango", "Apple", 'Ford', 'BMW', 'Volvo']

10.index()

list = [1, 2, 4, "Mango", "Apple"]
list.index("Mango"))

OUTPUT = 3

11.reverse()

list = [1, 2, 4, "Mango", "Apple"]
list.reverse()

OUTPUT = ['Apple', 'Mango', 4, 2, 1]

# About Tuples

Tuples are used to store multiple items in a single variable. Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage. A tuple is a collection which is ordered and unchangeable.
It is written with round brackets.

example:
   mytuple = ("apple", "banana", "cherry")
   print(mytuple)



------------------------------------------------------------------------------------------
Assignment 2


# Complete Methods of Dictionary From w3schools:


i)clear()
  
  It clears all the elements.

eg:

Fruits = {
   "type" : "Orange"
   "colour" : "orange"
   "shape" : "circle"
}
 Fruits.clear()
 print(Fruits) 

Output: {}


ii)copy()
 
 It basically copy the dictionary.

eg:

Fruits = {
   "type" : "Orange"
   "colour" : "orange"
   "shape" : "circle"
}
 Fruits.copy()
 print(Fruits) 

Output: { "type" : "Orange", "colour" : "orange", "shape" : "circle"}

iii)fromKeys()

  The fromkeys() method returns a dictionary with the specified keys and the specified value.

eg:

x = ('key1', 'key2', 'key3')
y = 0,1

dict = dict.fromkeys(x, y)
print(dict)

Output: {'key1': (0, 1), 'key2': (0, 1), 'key3': (0, 1)}

iv)get()

  Returns the value of a specified key

eg:

Fruits = {
   "type" : "Orange"
   "colour" : "orange"
   "shape" : "circle"
}
 x = Fruits.get("colour")
 print(x) 

Output: orange

v)items()

  Returns a list containing a tuple for each key value pair

eg:


Fruits = {
   "type" : "Orange"
   "colour" : "orange"
   "shape" : "circle"
}
 x = Fruits.items()
 print(x) 

Output: dict_items([('type', 'Orange'), ('colour', 'Orange'), ('shape', "circle")])

vi)Keys()

  Returns all the keys in the dictionary

eg:

 Fruits = {
   "type" : "Orange"
   "colour" : "orange"
   "shape" : "circle"
}
 x = Fruits.keys()
 print(x) 

Output: dict_keys(['type', 'colour', 'shape'])

vii)pop()

  It removes the the specified element which we want to remove

eg:

Fruits = {
   "type" : "Orange"
   "colour" : "orange"
   "shape" : "circle"
}
 x = Fruits.pop("shape")
 print(x) 

Output: {'type':'Orange', 'colour':'Orange'}

viii)popitem
  
   It removes the last item

eg:

Fruits = {
   "type" : "Orange"
   "colour" : "orange"
   "shape" : "circle"
}
 x = Fruits.popitem()
 print(x) 

Output: {'type':'Orange', 'colour':'Orange'}

ix)setdefault()

  It returns the value of a specified keys

eg: 

Fruits = {
   "type" : "Orange"
   "colour" : "orange"
   "shape" : "circle"
}
 x = Fruits.setdefault("type", "Apple")
 print(x) 

Output:Orange

x)update()

  Updates the dictionary with the specified key-value pairs

eg:


Fruits = {
   "type" : "Orange"
   "colour" : "orange"
   "shape" : "circle"
}
 x = Fruits.update({"type": "Apple"})
 print(x)
 
Output: {'type':'Apple', 'colour':'Orange', 'shape':'circle'}

xi)values()

  Returns a list of all the values in the dictionary

eg:

Fruits = {
   "type" : "Orange"
   "colour" : "orange"
   "shape" : "circle"
}
 x = Fruits.values()
 print(x)
 
Output: dict_values(['Orange', 'Orange', 'circle'])



# COMPLETE METHODS OF STRINGS:

1) capitalize()
   
    txt = "hello world."

    x = txt.capitalize()

    print (x)

Output:Hello world

  
2) casefold()	
    
    txt = "Hello World!"
    
    x = txt.casefold()

    print(x)

output:hello world! 

   
3) center()
     
    txt = "car"

    x = txt.center(20)

    print(x)

output:     car       
	
4) count()	
 
    txt = "I love apples"

    x = txt.count("apple")

    print(x)

output: 2
        
5) encode()

    txt = "My name is Ståle"

    x = txt.encode()

    print(x)
	
output:	b'My name is St\xc3\xe5le'  

6) endswith()	
 
    txt = "Hello, welcome to my world."

    x = txt.endswith(".")

    print(x)

output:True 

7) expandtabs()

    txt = "H\te\tl\tl\to"

    x =  txt.expandtabs(2)

    print(x)
	
output:H e l l o		

8) find()

    txt = "Hello, welcome to my world."

    x = txt.find("welcome")

    print(x)
	
Output:7	
    
9) format()

    txt = "For only {price:.2f} dollars!"
    print(txt.format(price = 49))

output:For only 49.00 dollars!
	
10) isalnum() 	

    txt = "Company12"

    x = txt.isalnum()

    print(x)
	
output:True	
        
11) index()

     txt = "Hello, welcome to my world."

     x = txt.index("welcome")

     print(x)
	
output:	7

12) isalpha()	

     txt = "CompanyX"

     x = txt.isalpha()

     print(x)
	
output:True	
        
13) isascii()

     txt = "Company123"

     x = txt.isascii()

     print(x) 
	
output:True	

14) isdecimal()

    txt = "\u0033" #unicode for 3

    x = txt.isdecimal()

    print(x)
	
output:True		

15) isdigit()	

    txt = "50800"

    x = txt.isdigit()

    print(x)
	
output:True	   

16) replace()	

        txt = "I like bananas"

        x = txt.replace("bananas", "apples")

        print(x)
	
output:I like apples
	
17) split()	

        txt = "welcome to the jungle"

        x = txt.split()

        print(x)
	
output:['welcome', 'to', 'the', 'jungle']	

18) splitlines()	

        txt = "Thank you for the music\nWelcome to the jungle"

        x = txt.splitlines()

        print(x)
	
output:['Thank you for the music', 'Welcome to the jungle']
       
19) startswith()	

        txt = "Hello, welcome to my world."

	x = txt.startswith("Hello")

	print(x)
	
output:True	

20) strip()	

       txt = "     banana     "

	x = txt.strip()

	print("of all fruits", x, "is my favorite")

output:of all fruits banana is my favorite
	
21) swapcase()	

        txt = "Hello My Name Is PETER"

	x = txt.swapcase()

	print(x)

output:hELLO mY nAME iS peter
	
22) title()	

        txt = "Welcome to my world"

	x = txt.title()

	print(x)

output:Welcome To My World

23) translate()	
       
        mydict = {83:  80}
	txt = "Hello Sam!"
	print(txt.translate(mydict))
	
output:Hello Pam!

24) upper()	
        
       txt = "Hello my friends"

	x = txt.upper()

	print(x)
	
output:HELLO MY FRIENDS
	
25) zfill()

       txt = "50"

	x = txt.zfill(10)

	print(x) 
	
output:0000000050
	
26) rstrip()

        txt = "     apple     "

	x = txt.rstrip()

	print("of all fruits", x, "is my favorite")
	
output:of all fruits      apple is my favorite
	
27) rsplit()

      txt = "apple, banana, cherry"

      x = txt.rsplit(", ")

      print(x)
	
output:['apple', 'banana', 'cherry']
	
28) rpartition() 

      txt = "I could eat bananas all day, bananas are my favorite fruit"

      x = txt.rpartition("bananas")

      print(x)
	
output:('I could eat bananas all day, ', 'bananas', ' are my favorite fruit')
	
29) rjust()

	txt = "banana"

	x = txt.rjust(20)

	print(x, "is my favorite fruit.")
	
output:              banana is my favorite fruit.
	
30) rindex()

	txt = "Mi casa, su casa."

	x = txt.rindex("su")

	print(x)
	
output:9

31)rfind()

	txt = "Mi casa, su casa."

	x = txt.rfind("casa")

	print(x)
	
output:12

32)partition()

	txt = "I could eat bananas all day"

	x = txt.partition("bananas")

	print(x)
	
output:('I could eat ', 'bananas', ' all day')

33)maketrans()

	txt = "Hello Sam!"

	mytable = txt.maketrans("S", "P")

	print(txt.translate(mytable))
	
output:Hello Pam!

34)lower()

	txt = "Hello my FRIENDS"

	x = txt.lower()

	print(x)
	
output:hello my friends

35)Istrip()

	txt = "     banana     "

	x = txt.lstrip()

	print("of all fruits", x, "is my favorite")
	
output:of all fruits banana     is my favorite

36)Ijust()

	txt = "orange"

	x = txt.ljust(20)

	print(x, "is my favorite fruit.")
	
output:orange               is my favorite fruit.
	
37)join()

	myTuple = ("John", "Peter", "Vicky")

	x = "#".join(myTuple)

	print(x)
	
output:John#Peter#Vicky

38)isupper()

	txt = "this is a book!"

	x = txt.isupper()

	print(x)
	
output:False

39)istitle()

	txt = "Hello, And Welcome To My World!"

	x = txt.istitle()

	print(x)

output:True
	
40)isspace()

	txt = "   "

	x = txt.isspace()

	print(x)

output:True
	
41)isprintable()

	txt = "Hello! Are you #1?"

	x = txt.isprintable()

	print(x)

output:True
	
42)isnumeric()

	txt = "565543"

	x = txt.isnumeric()

	print(x)

output:True

43)islower()

	txt = "HELLO WORLD!"

	x = txt.islower()

	print(x)

output:False

44)isidentifier()

	txt = "Hello"

	x = txt.isidentifier()

	print(x)

output:True




