#function to get Feet
def Feet(inch):
    feet = inch/12
    print("=============Conversion===============")
    print("Inch to Feet: "+ str(feet))

#function to get yards
def Yard(inch):
    yard = inch/36
    print("=============Conversion===============")
    print("Inch to Yard: "+ str(yard))


inch = int(input("Enter inch value to convert: "))
Feet(inch)
Yard(inch)
