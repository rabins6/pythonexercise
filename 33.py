gender=input("Input your gender (M for male and F for female) = ")
HV=float(input("Hemoglobin value(g/l) = "))
if gender == "M" :
    if 134 <= HV <= 167:
        print("NORMAL")
    elif HV < 134 :
        print("LOW")
    else:
        print("HIGH")
elif gender == "F":
    if 117 <= HV <= 155:
        print("NORMAL")
    elif HV < 117:
        print("LOW")
    else:
        print("HIGH")
else:
    print("INVALID GENDER. Input your gender (M for male and F for female)")