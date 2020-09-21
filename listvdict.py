list=list()
dict=dict()
list.append(27)
list.append('F')
list.append('Priyanka')
print(list)
dict['Age']=27
dict['Gender']='F'
dict['Name']='Priyanka'
print(dict)
list.pop(1)
#or list.remove('F')
#dict.pop('Gender') #removes the value for the desired key provided in parameter
res=dict.popitem() #t removes the last inserted key-value pair from the dictionary and returns it as a tuple.
print(list)
print(dict)
print(res)
