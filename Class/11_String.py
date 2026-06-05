#String literals:
s = "hello"
a = 'hello_a'
b = """hello_b"""
c = '''hello_c '''

#Length of a string:

length = len(s)
print(s)
print(length)

#Traversal:
print(s[0])#0 --> 1st from start
print(s[4]) #4 --> 5th from start 
print(s[-1]) #-1 --> 1st from last 

#one way of traversal:
#Method_1
for x in s:
    print(x,end='')
#Method_2 
for x in range(len(s)): # from 0 to len(s) i.e 5 gives 0,1,2,3,4
    print(s[x],end='')

#Slicing : Operator "[]" defined as s[start:stop:step]-> just like a range function

d="hello world"
print(d[0:7]) #OR
print(d[:7])  #--> if no start is given '0' is taken as default 
print(d[3:7])
#print(d[-5:-9]) --> This is invalid the start should always be less than stop or we say that slicing is always done in the forward direction WHEN steps are positive
print(d[-4:-1])
print(d[0:15:2])#--> If stop > last index in string then its value is set to the last index+1 by default
print(d[::2]) #--> defualt values are taken in case of empty parameters, start = 0, stop = len(d), step = 2
print(d[::])#--> All empty means no slicing so prints the entire string as is 
print(d[::-1])#--> Reverse order 
print(d[-3:-9:-1])#--> Since steps are negative, start > stop 
print(d[7:1:-1])#--> Reverse slicing using positive start/stop



#Sting operations 

a="pranjal"
b="verma"
c = 'tiya'
print(a+b)#--> 1.concatenation using '+'
print(a*10+b)#--> 2.repetion using '*'
print("a" in a)#--> 3.membership using 'in /not in', gives a boolean value
print('z'not in b)
print('ia' in  c)

#--> 4.comparison of string is done in lexical or dictionary order:-
# suppose we have these strings 
a = "apple"
b = "ball"
c = 'cat'
d = 'dog'
p = 'python'
# Now in lexical order this will be the case : apple < ball < cat < dog < python
#->apply>apple because 'y' comes latter than 'e' in the dictionary 
#->cat < catch becasue 'catch' has extra letters 
#->data > Data because in ASCII chart capital letters and numbers come before lowecase letters 
#->2nd < Byte because numbers come before letters in ASCII index
print(a>b)
