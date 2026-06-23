#===> int() conversion
a=10.56 #float
b=True  #boolean
c='pranjal' #string_1
d='123' #string_2 
binary='0b1010' #string_3

print(int(a))   # this will give the floor of a=10.56
print(int(b))   # this converts the following boolean variable 'b' to int i.e. 1
# print(int(c))   # Now this will give you an error as string_1 is not a valid string for conversion to int
print(int(d))   #Unlike string_1, string_2 is a valid string as it contains numeric values
print(int(binary,2)) # this 2 is provided to let the compiler know that the number in the string is a binary literal ( base 2)


### For complex numbers it doesn't work

#===> float conversion
x=10
print(float(x))
print(float(b))
print(float(d))
# print(float(e,2))   # this will throw an error because 'float()', by defination takes only one parameter (i.e. there is no float(x, base) function in python library)

#===> bool() conversion
a=2 
b=1
c=0
print(bool(a),bool(b),bool(c))      #any integer '>= 1' when converted to boolean gives 'True' as the value in boolean
print(bool(2+4j))       #complex numbers are accepted by 'bool()' function 
print(bool(21.34))      # As a rule of thumb, bool(anythihgn)=True and bool(0)=False
print(bool('ar'))       # for a string as well this give bool(string) = True
print(bool())           # 'bool()' function without any parameters gives you 'False'