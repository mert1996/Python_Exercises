import cmath

coordinates = complex(input())

polar = cmath.polar(coordinates)
modulus = polar[0]
print(modulus)
print(cmath.phase(coordinates))
