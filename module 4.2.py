while True:
    inches = float(input("enter the lenght in inches (negative value to stop):"))
    if inches < 0:
        print("program end. bye bye!")
        break

    centimeters = inches * 2.54
    print(f"{inches} inches is equel to {centimeters:.2f} centimeters")



