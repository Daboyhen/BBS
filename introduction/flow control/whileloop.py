#while loop with else statement
print('\n show while loop with else statement')
count=0
while count <4:
    print('my count is less than 4')
    count = count +1
else:
    print('my count is not less than 4')



#reverse using while loop 
print('\nshow reverse using while loop in python ')
my_list =['welcome','to','python 3','programming']
r= len(my_list)-1
while r>=0:
    print(my_list[r])
    r=r-1


#while else
print('\nwhile else')
num =3
while num >0:
    num= num -1
    print(num)
else:
        print('the end of loop')



#infinite while loop 
print('\ninfinite while loop')
while  True:
    print('welcome to loop')
 #end of code



#continue statement in python
value =1
while value <7:
    value= 7
    value=value+1 
    if value==4:
        continue
    print(value)
    #end of code