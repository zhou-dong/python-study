# --- Example One: back knowledge of complex number ---
def basic_knowledge():
    x = 1 + 3j #(x-1)**2 = -9, x = 1 + 3j 
    print x
    print (x-1)**2
    print type(x)

# ax + b = c
def solve(a, b, c):
    return (c-b)/a

# 10x + 5 = 30
print solve(10.0, 5.0, 30.0) 
# (10 + 5i)x + 5 = 20
print solve(10+5j, 5.0, 20.0)

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors

# --- Example Two: interpert complex numer as a point in the plane ---
def complex_as_point():
    number_list = [2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1j]
    plt.title("Interpert Complex Number")
    plt.xlabel("Real Number")
    plt.ylabel("Imaginary Number")
    for number in number_list:
        plt.scatter(number.real, number.imag)
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.grid(True)
    plt.show()

# --- Example Three: Complex numbers As arrows ---
def complex_as_arrow():
    z = -6 + 5j
    plt.title("Complex as Arrow")
    plt.xlabel("Real Number")
    plt.ylabel("Imaginary Number")
    plt.arrow(0, 0, z.real, z.imag)
    plt.xlim(-10,10)
    plt.ylim(-10,10)
    plt.grid(True)
    plt.show()

# --- Example Four: Complex Composition ---
def complex_composition(x, y):
    z = x + y
    plt.title("Complex Composition")
    plt.xlabel("Real Number")
    plt.ylabel("Imaginary Number")
    plt.arrow(0, 0, x.real, x.imag, color='g')
    plt.arrow(0, 0, y.real, y.imag, color='b')
    plt.arrow(0, 0, z.real, z.imag, color='r')
    plt.xlim(-3,6)
    plt.ylim(-3,6)
    plt.grid(True)
    plt.show()
#complex_composition(2+3j, 3+1j) 

# --- Example Five: Mutiply Complex Number ---
def multiply_complex(complex_number, time):
    z = time * complex_number
    plt.title("Multiply Complex")
    plt.xlabel("Real Number")
    plt.ylabel("Imaginary Number")
    plt.arrow(0, 0, complex_number.real, complex_number.imag, color='b')
    plt.arrow(0, 0, z.real, z.imag, color='y')
    plt.xlim(-3,3)
    plt.ylim(-3,3)
    plt.grid(True)
    plt.show()
#multiply_complex(2 + 2j, -1)

# --- Example Six: Rotate Complex Number 90 degree ---
# Need x + yi mapping to y + xi
# f(z) = iz
def rotate_ninty_degree(complex_number):
    z = 1j * complex_number
    plt.title("Multiply Complex")
    plt.xlabel("Real Number")
    plt.ylabel("Imaginary Number")
    plt.arrow(0, 0, complex_number.real, complex_number.imag, color='b')
    plt.arrow(0, 0, z.real, z.imag, color='y')
    plt.xlim(-3,3)
    plt.ylim(-3,3)
    plt.grid(True)
    plt.show()
#rotate_ninty_degree(2+2j)
