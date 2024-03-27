import random
# Simulando 100 números para winrate, kda e kp
winrate_list = [random.uniform(0, 100) for _ in range(100)]
kda_list = [random.uniform(0, 10) for _ in range(100)]
kp_list = [random.uniform(0, 1) for _ in range(100)]

# Fórmula 1
results1 = [round((winrate*1 + kda*10.0 + kp*2.0) / 3) for winrate, kda, kp in zip(winrate_list, kda_list, kp_list)]

# Fórmula 2
results2 = [round((winrate*0.5 + kda*5.0 + kp*1.0) / 3) for winrate, kda, kp in zip(winrate_list, kda_list, kp_list)]

# Fórmula 3
results3 = [round((winrate*2 + kda*10.0 + kp*1.5) / 3) for winrate, kda, kp in zip(winrate_list, kda_list, kp_list)]

# Exibindo os resultados no console
print("Resultados da Fórmula 1:", results1)
print("Resultados da Fórmula 2:", results2)
print("Resultados da Fórmula 3:", results3)
