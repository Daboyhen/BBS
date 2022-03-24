#datatype
fish =22


print(fish, 'is of type type',(fish))

#fish =22
#print(fish, 'is oftype', type (fish))

weight = 5.05
print (weight ,'is of type', type(weight))

#data type2. pyton list
print('print my list below:')
mylist =['digikids', 458, 20 , 74.93 , 'students']
print (mylist)

print('extracting an item from the list')
print('my list [1]',mylist[1])
print('my list[0] list item is :', mylist[0])

#show range
print('list range')
mylist = ['digikids',458, 20, 74, 93, 'students', 56, 20, 45, 'pc', 21]
print('mylist[2:6] is:', mylist[2:6])
print('mylist[2:6] is:', mylist[2:20])

#show range
print ('list range')
mylist =['micheal',44, 'ndungu',68,4468,'ksi',2,'ball',4,405, 'cop',7,'king','jungle',63]
print('my list [10]', mylist [1])
print('mylist[5:7] is',mylist[5:7])

mylist = ['digikids',458, 20, 74, 93, 'students', 56, 20, 45, 'pc', 21]
mylist [0] = 'coder'
mylist[3] =89
mylist [4] ='tear'
print (mylist)

#data type 3. python tuple
print('this are my tuples:')
myvar =(14,'digikids',4.5,'my class',57,6.7)
print(myvar)
print('myvar[3] is:',myvar[3])
# myvar[1]=10

#data type 4. python strings
print('this are python strings:')
greetings ='how are you?'
print(greetings)
hello ='how are you today? will you go to swimming in the afternoon'
print(hello)
#tripple quotes
awesome ='''
how are you?
have you eaten?
will you go to swimming
in the afternoon
'''
print(awesome) 


good ="how are you?"
print("extract good[2]:is",good[5])
print(good[2:8])
#good[1] =0


#data types 5. python set
print('print the ordered list')
books ={40,34,2,2,6,6,8,8,8,8,40,15,'digikids','digikids','Digikids'}
print(books)
print(type(books))
print(books[6])
#set object does not support indexing:  print(books[4])


#data types 6. python dictionary
digikids ={'student':12,'student1':8,'student2':15, \
    2:'parent'
}
print(digikids[2])
#print(digikids['parent'])