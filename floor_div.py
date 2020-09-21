from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

try:
    a=int(a)
    b=int(b)
except:
    print('Invaid input')
print(a//b)
print(a/b)
