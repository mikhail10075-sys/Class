def cube(x):
  return x**3

x = float(input("Enter a number you wish to cube: "))

if x % 3 == 0:
    y = cube(x)
    print(y)

else :
    print("Number is not divisible by 3")