1.
a=int(input('enter your age'))
if a>=18:
    print('you can vote')
else:
    print('you are too young to vote')
2.  
b=int(input('enter a number'))
if b%2==0:
    print(b,'is even')
else:
    print(b,'is odd')
3.   
c=float(input('enter your monthly sales'))
if c>=40000:
    print('your commision is',c*0.15)
else:
    print('your commision is',c*0.05)
4.
d=float(input('enter a number'))
if d<0:
    print('your number is less than 0')
if d==0:
    print('your number is 0')
if d>0:
    print('your number is more than 0')
5.    
e=float(input('enter a number'))
if e>=0:
    print(e)
if e<0:
    print(e*-1,)
6.    
f=float(input('enter a number'))
if f%2==0:
    print(f,'is even')
if f==0:
    print(f,'is zero')
if f<0:
    print(f,'is negative')
else:
    print(f,'is odd')
7.
g=int(input('enter username'))
if g==admin:
    h=input('enter your password')
    if h=='admin123':
        print('access granted')
if g:
    print('incorrect username')
