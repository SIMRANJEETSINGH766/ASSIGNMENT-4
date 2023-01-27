LeapYear = int(input("Enter year: "))
if LeapYear % 400 == 0 :
    print(LeapYear, "is a Leap Year")
elif LeapYear % 100 == 0 :
    print(LeapYear, "is not a Leap Year")
elif LeapYear % 4 == 0 :
    print(LeapYear, "is a Leap Year")
else :
    print(LeapYear, "is not a Leap Year")
