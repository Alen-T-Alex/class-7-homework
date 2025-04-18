print("match with a study buddy")
grade=int(input("what is your grade?? options are from 9th to 12th. "))
sub=str(input("what is your subject. eg: science,math,english. "))
time=int(input("how long do you need someone to study with? "))
print("matching")
if grade<=10:
    if sub=="science":
        print("your study partner is Alex for 5$ an hour")
    elif sub=="math":
        print("your study partner is Sam for 6$ an hour")
    else:
        print("your study partner is Riley for 5$ an hour")
else:
    if sub=="math":
        if time<=3:
            print("your partner is Taylor for 7$ an hour")
        else:
            print("your partner is Jordan for 8$ an hour")
    elif sub=="science":
        print("your partner is Casey for 7$ an hour")
    else:
        print("your partner is Morgan for 6$ an hour")
