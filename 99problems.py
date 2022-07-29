value = int(input())

if (value < 99):
    print(99)
else:
    hundredth = value % 100
    if (hundredth == 0):
        print(value - 1)
    else:
        if ((99 - hundredth) > 50):
            print(value - (hundredth + 1))
        elif(99 - hundredth == 50):
            print (value + 50)
        else:
            print(value + (99 - hundredth))

# See alternative method: https://github.com/ecly/kattis/blob/master/99problems/99problems.py