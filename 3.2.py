name = input("Enter cabin class (in block) =  ")
if name == ("LUX"):
    print("upper-deck cabin with a balcony.")
elif name ==("A"):
    print("above the car deck, equipped with a window.")
elif name==("B"):
    print("windowless cabin above the car deck.")
elif name ==("C"):
    print("windowless cabin below the car deck.")
else:
    print("INVALID CABIN CLASS")