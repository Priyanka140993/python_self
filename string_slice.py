def merge_the_tools(string, k):
    l=int(len(string))
    n=int(l/k)
    i=0
    while i<=l:
        str=string[i:n]
        #print(str)
        i=n
        n=n+n
        print(removeDup(str))

from collections import OrderedDict
def removeDup(str):
    return "".join(OrderedDict.fromkeys(str))

string = input( )
k=int(input('/'))
merge_the_tools(string, k)
