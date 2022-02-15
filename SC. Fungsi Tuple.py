print ('<SOURCE CODE FUNGSI>')
print ('TUGAS FUNGSI 1')
def massage (number) : 
    print ("Enter a number:", number)

number = 1234 
massage (1)
print (number)

print ('TUGAS FUNGSI 2')
def message (what, number) : 
    print ("Enter", what, "number", number)

#invoke the function 
message ("telephone", 11)
message ("price", 5)
message ("number", "number")

print ('TUGAS FUNGSI 3')
def my_function (a, b, c) : 
    print (a, b, c)
my_function (1, 2, 3) 
print ()

def introduction (first_name, last_name): 
    print ("hello, my name is", first_name, last_name)
introduction ("skywalker", "luke")
introduction ("quick", "jesse")
introduction ("kent", "clark")
print ()

def introduction (first_name, last_name) :
    print ("hello, my name is", first_name, last_name)
introduction ("luke", "skywalker")
introduction ("jesse", "quick")
introduction ("clark", "kent")

print ('TUGAS FUNGSI 4')
def introduction (first_name, last_name) : 
    print ("hello, my name is", first_name, last_name)
introduction (first_name = "james", last_name = "bond")
introduction (last_name = "skywalker", first_name = "luke")

print ('TUGAS FUNGI 5')
def adding (a, b, c) : 
    print (a, "+", b, "+", c, "=", a + b + c)

adding (1, 2, 3)
adding (c = 1, a = 2, b = 3)
adding (3, c = 1, b = 2)
adding (4, 3, c = 2) 

print ('TUGAS FUNGSI 6')
print ('tugas 6a : ')
def list_sum (Ist) : 
    s = 0 
    for elem in Ist : 
        s += elem 
    return s 
print (list_sum ([5, 4, 3]))

print ('tugas 6b : ')
def list_sum (Ist) : 
    s = 0 
    for elem in Ist : 
        s += elem 
    return s 
print (list_sum ([5]))

print ('tugas 6c')
def strange_list_fun (n): 
    strange_list = []

    for i in range (0, n): 
        strange_list.insert(0, i)

    return strange_list 
print (strange_list_fun(5)) 

print ('TUGAS FUNGSI 7')
def bmi (weight, height) : 
    return weight / height ** 2 
print (bmi(52.5, 1.65))

print ('TUGAS FUNGSI 8')
print ('tugas 8a : ')
def is_a_triangle (a, b, c) : 
    if a + b <= c:
        return False 
    if b + c <= a: 
        return False
    if c + a <= b: 
        return False
    return True 

print (is_a_triangle(1, 1, 1))
print (is_a_triangle(1, 1, 3))

print ('tugas 8b :')
def is_a_triangle (a, b, c) :  
    return a + b > c and b + c > a and c + a > b 
print (is_a_triangle(1, 1, 1))
print (is_a_triangle(1, 1, 3))

print ('tugas 8c :')
def is_a_triangle (a, b, c) : 
    if a + b <= c or b + c <= a or c + a <= b : 
        return False
    return True

print (is_a_triangle(1, 1, 1))
print (is_a_triangle(1, 1, 3))

print ('TUGAS FUNGSI 9')
def is_a_tringle (a, b, c) :
    return a + b > c and b + c > a and c + a > b 

def heron (a, b, c) : 
    p = (a + b + c) / 2 
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5 

def area_of_triangle (a, b, c) : 
    if not is_a_tringle (a, b, c) : 
        return None
    return heron (a, b, c)

print (area_of_triangle(1., 1., 2. ** .5))