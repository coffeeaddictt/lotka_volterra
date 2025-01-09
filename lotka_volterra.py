import matplotlib.pyplot as plt
import pandas as pd

#Partie 1: Euler method implementation
print("Partie 1: Testing basic implementation")

time = [0]
lapin = [1000]
renard = [2000]

alpha = 1/3
beta = 1/3
delta = 1/3
gama = 1/3

step = 0.001

for i in range(1000):
    new_value_time = time[-1] + step
    new_value_lapin = (lapin[-1] * (alpha - beta * renard[-1])) * step + lapin[-1]
    new_value_renard = (renard[-1] * (delta * lapin[-1] - gama)) * step + renard[-1]
    