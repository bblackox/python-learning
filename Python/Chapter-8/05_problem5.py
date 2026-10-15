# Write a python function which converts inches to cms

def inches_to_cm(inch):
    return inch * 2.54

n = int(input("Enter the value in inches: "))
print(f"the corresponding value in cm is {inches_to_cm(n)}")