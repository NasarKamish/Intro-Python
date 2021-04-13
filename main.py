print("Hello World")
# this code is used to display "Hello World"

_PI = 3.14
# this is seen as a constant

r = float(input("Enter Radius:"))
Area = _PI * r * r
# or do r**2
print("The area of your circle is: " + str(Area))
# this code gets the radius from the user and then displaying the Radius of the circle

Diameter = r + r
print("The diameter of your circle is: " + str(Diameter))
# this code uses the radius to calculate and display the diameter of the circle

Circumference = 2 * _PI * r
print("The circumference of your circle is: " + str(Circumference))
# this code uses the radius to calculate and display the circumference
