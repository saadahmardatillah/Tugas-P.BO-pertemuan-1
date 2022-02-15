print ('a. PERCOBAAN TUPLE 1')
print ('a.1')
my_tuple = tuple ((1, 2, "string"))
print (my_tuple)

my_list = [2, 4, 6]
print (my_list) #outputs: [2, 4, 6]
print (type(my_list)) #outputs: <class 'list'> 
tup = tuple (my_list)
print (tup) #outputs: (2, 4, 6)
print (type(tup)) #outputs: <class 'tuple'> 

print ('b.2') 
my_tuple = (1, 10, 100)
t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3 

print (len(t2))
print (t1)
print (t2)
print (10 in my_tuple)
print (-10 not in my_tuple)

print ('b. PERCOBAAN LIBRARY 1')
print ('b.1')
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss' : 5551234567, 'suzy' : 22657854310}
empty_dictionary = {}

#print the values here. 
print (phone_numbers['suzy'])

print ('b.2')
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary. keys () : 
    print (key, "->", dictionary[key]) 

print ('b.3') 
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for word in words : 
    if word in dictionary : 
        print (word, "->", dictionary [word]) 
    else: 
        print (word, "is not in dictionary")

print ('c. PERCOBAAN TUPLE DENGAN LIBRARY')
school_class = {}

while True: 
    name = input ("enter the student's name: ")
    if name == '' : 
        break 
    score = int (input ("enter the student's score (0-10: "))
    if score not in range (0, 11) : 
        break 
    if name in school_class : 
        school_class [name] += (score, )
    else: 
        school_class [name] = (score, )
    
for name in sorted (school_class.keys()) : 
    adding = 0 
    counter = 0 
    for score in school_class[name] : 
        adding += score 
        counter += 1
    print (name, ":", adding / counter)

print ('PENUGASAN EXCEPTION')
print ('a. Percobaan 1')
try : 
    value = int(input('enter a natural number: '))
    print ('the reciprocal of', value, 'is', 1/value) 
except : 
    print (' i do not know what to do. ')

print ('b. Percobaan 2')
while True: 
    try: 
        number = int(input("enter an int number: "))
        print (5/number)
        break 
    except ValueError:  
        print ("wrong value.")
    except ZeroDivisionError: 
        print ("sorry. i cannot divide by zero.")
    except: 
        print ("i don't know what to do...") 

print ('c. Percobaan 3')
try: 
    value = int(input("enter a value: ")) 
    print(value/value)
except ValueError: 
    print ("bad input...")
except ZeroDivisionError: 
    print ("very bad input...")
except: 
    print ("Booo!")