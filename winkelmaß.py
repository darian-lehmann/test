from math import pi

b = input ("Geben Sie einen Winkel in Bogenmaß ein:")
b = float (b)

g = (360/(2*pi))*b

bogenminute = g * 60
bogensekunde = bogenminute * 60

print (g, "°", bogenminute, ",", bogensekunde, ",," )
