def lowest(n1, n2, n3):
    if n1 < n2 and n1 < n3: 
        print(f"The lowest number is {n1:.2f}.")
    else:
        if n2 < n1 and n2 < n3:
            print(f"The lowest number is {n2:.2f}.")
        else:
            if n3 < n1 and n3 < n2:
                print(f"The lowest number is {n3:.2f}.")

number1 = float(input("Insert first number: "))
number2 = float(input("Insert second number: "))
number3 = float(input("Insert third number: "))

lowest(number1, number2, number3)