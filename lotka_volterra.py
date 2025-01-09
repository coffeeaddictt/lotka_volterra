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


#fixing the runtime error
    max_population = 1e6
    new_value_lapin = max(0, min(new_value_lapin, max_population))
    new_value_renard = max(0, min(new_value_renard, max_population))


   
    time.append(new_value_time)
    lapin.append(new_value_lapin)
    renard.append(new_value_renard)

plt.figure(figsize=(15, 6))
plt.plot(time, lapin, "b-", label="Rabbits")
plt.plot(time, renard, "r-", label="Foxes")
plt.title("Test of Lotka-Volterra Model")
plt.legend()
plt.show()


#Partie 2: Parameter Optimization
print("\nPart 2: Finding best parameters")

print("Loading data...")
data = pd.read_csv('/Users/sanae/Downloads/populations_lapins_renards.csv')


test_values = [1/3, 2/3, 1, 4/3]

best_error = 999999999
best_alpha = 0
best_beta = 0
best_delta = 0
best_gama = 0
best_lapin = None
best_renard = None