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

total = len(test_values)**4
current = 0

for alpha in test_values:
    for beta in test_values:
        for delta in test_values:
            for gama in test_values:
                current += 1
               
                time = [0]
                lapin = [data['lapin'][0]]
                renard = [data['renard'][0]]
               
                for i in range(len(data)):
                    new_value_time = time[-1] + step
                    new_value_lapin = (lapin[-1] * (alpha - beta * renard[-1])) * step + lapin[-1]
                    new_value_renard = (renard[-1] * (delta * lapin[-1] - gama)) * step + renard[-1]
                   
                    max_population = 1e6  
                    new_value_lapin = max(0, min(new_value_lapin, max_population))
                    new_value_renard = max(0, min(new_value_renard, max_population))


                    time.append(new_value_time)
                    lapin.append(new_value_lapin)
                    renard.append(new_value_renard)

                    # calculating MSE
                error_lapin = 0
                error_renard = 0
                for i in range(len(data)):
                    error_lapin += (data['lapin'][i] - lapin[i])**2
                    error_renard += (data['renard'][i] - renard[i])**2
                total_error = (error_lapin + error_renard) / (2 * len(data))
               
                if total_error < best_error:
                    best_error = total_error
                    best_alpha = alpha
                    best_beta = beta
                    best_delta = delta
                    best_gama = gama
                    best_lapin = lapin.copy()
                    best_renard = renard.copy()
                    print(f"\nFound better parameters!")
                    print(f"alpha (rabbit growth) = {alpha}")
                    print(f"beta (rabbit death from foxes) = {beta}")
                    print(f"delta (fox growth from eating) = {delta}")
                    print(f"gama (fox death rate) = {gama}")
                    print(f"MSE = {total_error}\n")

print("\nBest parameters found:")
print(f"alpha = {best_alpha}")
print(f"beta = {best_beta}")
print(f"delta = {best_delta}")
print(f"gama = {best_gama}")
print(f"Final MSE = {best_error}")

# plot comparison of best model vs real data
plt.figure(figsize=(15, 6))
plt.plot(data['lapin'], 'b.', label='Real Rabbits', alpha=0.5)
plt.plot(data['renard'], 'r.', label='Real Foxes', alpha=0.5)
plt.plot(best_lapin, 'b-', label='Model Rabbits')
plt.plot(best_renard, 'r-', label='Model Foxes')
plt.title('Model vs Real Data')
plt.legend()
plt.show()