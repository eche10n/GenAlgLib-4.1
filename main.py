from pyeasyga import pyeasyga
import numpy as np
import pandas as pd
import math
import json

# Запись данных
raw_data = pd.read_csv('25.txt', sep = ' ', names = ['weight','volume','price'], engine = 'python', header=None)
weight_carrying  = raw_data['weight'][0]
capacity = raw_data['volume'][0]
raw_data = raw_data.drop([0])
data_size = raw_data.shape[0]
data = []
for i in range(0,data_size):
    data.append((raw_data['weight'][i+1], raw_data['volume'][i+1], raw_data['price'][i+1]))

# Инициализация
ga = pyeasyga.GeneticAlgorithm(data)
ga.population_size = 200


# Функция приспособленности
def fitness(individual, data):
    weight, volume, price = 0, 0, 0
    for (selected, item) in zip(individual, data):
        if selected:
            weight += item[0]
            volume += item[1]
            price += item[2]
    if weight > weight_carrying or volume > capacity:
        price = 0
    return price

# Установка функции приспособленности
ga.fitness_function = fitness
ga.run()
result_tuple = ga.best_individual()
print("Items in knapsack:\n")
for i in range(0,data_size):
    if (result_tuple[1][i]):
        print(data[i])
print("\nTotal price of these items:\n\n",result_tuple[0])
print("\nItems in data list:\n\n", result_tuple[1])
