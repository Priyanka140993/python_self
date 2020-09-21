d={'jane':1,'Michael':3,'Petra':2,'Rafael':5,'Alba':8,'Xiomara':4}
name=input('Enter Name: ')
print(name)
x=d.get(name,0)# search and return value of the key provided
#get(name) can be used will return none
print(x)
print(d)
