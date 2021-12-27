import math
print("Please enter the voltage:")
voltage_string = input()
voltage_int = float(voltage_string)

print("Please enter the resistance:")
resistance_string = input()
resistance_int = float(resistance_string)

print("")
power = (voltage_int ** 2) / resistance_int
print("The power is:")
print("{:.2f}".format(power))

# Conditionals
x = 6
if x == 6:
    print("x is 6")
