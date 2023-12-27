import random

# Parámetros del algoritmo
TARGET = "Hello, World!"
POP_SIZE = 100
GENES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789,.-;:_!'*#%&/()=?@${[]}"
MUTATION_RATE = 0.01

# Función para generar un individuo aleatorio (cadena)
def create_individual(size):
    return ''.join(random.choice(GENES) for _ in range(size))

# Función para calcular el fitness (qué tan cerca está de la cadena objetivo)
def fitness(individual):
    return sum(ch1 != ch2 for ch1, ch2 in zip(individual, TARGET))

# Función para el cruce de dos padres para crear un hijo
def crossover(parent1, parent2):
    index = random.randint(1, len(TARGET) - 1)
    return parent1[:index] + parent2[index:]

# Función para mutar un individuo
def mutate(individual):
    if random.random() < MUTATION_RATE:
        index = random.randint(0, len(individual) - 1)
        individual = list(individual)
        individual[index] = random.choice(GENES)
        individual = ''.join(individual)
    return individual

# Función para evolucionar la población
def evolve(population):
    new_population = []
    sorted_population = sorted(population, key=lambda x: fitness(x))
    for i in range(POP_SIZE):
        parent1 = random.choice(sorted_population[:50])
        parent2 = random.choice(sorted_population[:50])
        child = crossover(parent1, parent2)
        child = mutate(child)
        new_population.append(child)
    return new_population

# Crear la población inicial
population = [create_individual(len(TARGET)) for _ in range(POP_SIZE)]

# Ejecutar el algoritmo genético
generation = 0
while True:
    population = evolve(population)
    generation += 1
    fittest_individual = min(population, key=lambda x: fitness(x))
    if fitness(fittest_individual) == 0:
        break

print(f"Generación: {generation}, Mejor individuo: {fittest_individual}")
