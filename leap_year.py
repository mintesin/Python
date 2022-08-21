year=int(input("Please Enter the year: "))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("It is leap year")
        else:
            print("not leap year")
    else:
        print("It is leap year")
else:
    print("Not leap year")
