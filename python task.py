task 1

PI=3.14
radius = float(input('enter the radius of a circle:'))
area = PI*radius*radius
print("area of a circle = %.2f" %area)


task 2

filename = input("Input the filename:")
f_extns = filename.split(".")
print("the extension of the file is:" + repr(f_extns[-1]))
