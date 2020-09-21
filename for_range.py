if __name__ == '__main__':
    n = int(raw_input())
try:
    n=int(n)
except:
    print('Invalid input')
for i in range(n):
    print(i**2)
