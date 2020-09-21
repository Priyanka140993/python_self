def is_leap(year):
    leap = False
    try:
        yr=int(year)
    except:
        print('Invalid year')
    if (1900<=yr<=10**5):
        if yr%4==0:
            if yr%100==0:
                if yr%400==0:
                    leap= True
            else:
                leap = True
    # Write your logic here

    return leap

year = int(raw_input())
print is_leap(year)
