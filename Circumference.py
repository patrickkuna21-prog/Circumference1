def circumference(radius):
    pi=3.14
    result=2*pi*radius
    return result
r=float(input("Enter the radius of the circle:"))
answer=circumference(r)
print("The circumference of the circle is:", answer)