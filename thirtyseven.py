#5.5 review this is challenge 36 of the UTCP CODING BOOKLET
for i in range(0,4):
    dob = input("Enter Year of Birth\n>>> ")
    try:
        conv = int(dob)
        if conv >= 1903:
            if conv <= 2022:
                print("Your DOB is Valid")
                break
            else:
                print("Your DOB is Not Possible")
        else:
            print("Your DOB is Not Possible")
    except:
        print("Not A Parseable.")
    