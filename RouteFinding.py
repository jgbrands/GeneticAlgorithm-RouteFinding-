import random

graph = {
    'A':{'B': 1, 'C': 2},
    'B':{'A': 1, 'C': 1, 'D': 4},
    'C':{'A': 2, 'B': 1, 'D': 3},
    'D':{'B': 4, 'C': 3}
}

graph3 = {
    'A': {'B': 2, 'C': 3, 'D': 4},
    'B': {'A': 2, 'E': 5, 'F': 6},
    'C': {'A': 3, 'G': 7, 'H': 8},
    'D': {'A': 4, 'I': 9, 'J': 10},
    'E': {'B': 5, 'K': 11, 'L': 12},
    'F': {'B': 6, 'M': 13, 'N': 14},
    'G': {'C': 7},
    'H': {'C': 8},
    'I': {'D': 9},
    'J': {'D': 10},
    'K': {'E': 11},
    'L': {'E': 12},
    'M': {'F': 13},
    'N': {'F': 14}
}

graph4 = {
    'A': {'B': 1, 'C': 3, 'D': 2},
    'B': {'A': 1, 'E': 2, 'F': 1},
    'C': {'A': 3, 'F': 2, 'G': 1},
    'D': {'A': 2, 'G': 2, 'H': 3},
    'E': {'B': 2, 'I': 1, 'J': 2},
    'F': {'B': 1, 'C': 2, 'J': 3},
    'G': {'C': 1, 'D': 2, 'K': 1},
    'H': {'D': 3, 'K': 2, 'L': 1},
    'I': {'E': 1, 'M': 2, 'N': 1},
    'J': {'E': 2, 'F': 3, 'N': 2},
    'K': {'G': 1, 'H': 2, 'O': 3},
    'L': {'H': 1, 'O': 2, 'P': 1},
    'M': {'I': 2, 'Q': 1, 'R': 2},
    'N': {'I': 1, 'J': 2, 'R': 3},
    'O': {'K': 3, 'L': 2, 'S': 1},
    'P': {'L': 1, 'S': 2, 'T': 3},
    'Q': {'M': 1, 'U': 2, 'V': 1},
    'R': {'M': 2, 'N': 3, 'V': 2},
    'S': {'O': 1, 'P': 2, 'W': 3},
    'T': {'P': 3, 'W': 2, 'X': 1},
    'U': {'Q': 2, 'Y': 1, 'Z': 2},
    'V': {'Q': 1, 'R': 2, 'Z': 3},
    'W': {'S': 3, 'T': 2, 'Z': 1},
    'X': {'T': 1, 'Z': 2},
    'Y': {'U': 1},
    'Z': {'U': 2, 'V': 3, 'W': 1, 'X': 2}
}

graph5 = {
    '1': {'2': 2, '3': 5, '4': 1, '5': 3},
    '2': {'1': 2, '6': 4, '7': 3, '8': 1},
    '3': {'1': 5, '9': 2, '10': 3, '11': 4},
    '4': {'1': 1, '12': 5, '13': 3, '14': 2},
    '5': {'1': 3, '15': 1, '16': 2, '17': 4},
    '6': {'2': 4, '18': 3, '19': 2, '20': 1},
    '7': {'2': 3, '21': 4, '22': 2, '23': 5},
    '8': {'2': 1, '24': 4, '25': 3, '26': 2},
    '9': {'3': 2, '27': 1, '28': 4, '29': 3},
    '10': {'3': 3, '30': 2, '31': 1, '32': 4},
    '11': {'3': 4, '33': 1, '34': 2, '35': 3},
    '12': {'4': 5, '36': 2, '37': 3, '38': 4},
    '13': {'4': 3, '39': 1, '40': 2, '41': 5},
    '14': {'4': 2, '42': 4, '43': 1, '44': 3},
    '15': {'5': 1, '45': 2, '46': 3, '47': 4},
    '16': {'5': 2, '48': 4, '49': 3, '50': 1},
    '17': {'5': 4, '50': 2, '48': 3, '49': 1},
    '18': {'6': 3, '20': 2, '21': 5, '22': 1},
    '19': {'6': 2, '23': 4, '24': 3, '25': 1},
    '20': {'6': 1, '26': 5, '27': 2, '28': 3},
    '21': {'7': 4, '18': 5, '29': 1, '30': 2},
    '22': {'7': 2, '31': 3, '32': 5, '33': 4},
    '23': {'7': 5, '19': 4, '34': 3, '35': 1},
    '24': {'8': 4, '19': 3, '36': 2, '37': 5},
    '25': {'8': 3, '38': 4, '39': 5, '40': 2},
    '26': {'8': 2, '40': 4, '41': 3, '42': 1},
    '27': {'9': 1, '43': 4, '44': 3, '45': 2},
    '28': {'9': 4, '46': 1, '47': 5, '48': 3},
    '29': {'9': 3, '49': 2, '50': 1, '21': 1},
    '30': {'10': 2, '22': 5, '23': 3, '24': 1},
    '31': {'10': 1, '25': 5, '26': 2, '27': 3},
    '32': {'10': 4, '28': 1, '29': 5, '30': 2},
    '33': {'11': 4, '31': 5, '32': 3, '34': 1},
    '34': {'11': 2, '33': 1, '35': 5, '36': 4},
    '35': {'11': 3, '37': 2, '38': 1, '34': 5},
    '36': {'12': 4, '39': 2, '40': 1, '34': 4},
    '37': {'12': 3, '41': 5, '42': 1, '43': 2},
    '38': {'12': 2, '44': 3, '45': 1, '46': 4},
    '39': {'13': 1, '47': 3, '48': 4, '49': 2},
    '40': {'13': 2, '50': 4, '26': 4, '27': 3},
    '41': {'13': 5, '28': 2, '29': 1, '30': 4},
    '42': {'14': 4, '31': 1, '32': 2, '33': 5},
    '43': {'14': 3, '34': 2, '35': 1, '36': 1},
    '44': {'14': 1, '37': 3, '38': 5, '39': 4},
    '45': {'15': 2, '40': 1, '41': 5, '42': 4},
    '46': {'15': 3, '43': 1, '44': 5, '22': 2},
    '47': {'15': 4, '23': 2, '24': 5, '25': 1},
    '48': {'16': 4, '26': 3, '27': 2, '28': 5},
    '49': {'16': 3, '29': 4, '30': 1, '31': 2},
    '50': {'16': 1, '32': 5, '33': 4, '34': 3}
}

def saveToFile(string):
    with open('Log.txt', 'a') as f:
        f.write(string + '\n')

def appendToFile(string):
    with open('Log.txt', 'a') as f:
        f.write(string)

# Takes in a graph, a start node, and a finish node
# Returns a random route from start to finish or None if not found
def generateRoute(graph, start, finish):
    visited = set()
    route = [start]
    while route[-1] != finish:
        currentNode = route[-1]
        visited.add(currentNode)
        choices = [node for node in graph[currentNode] if node not in visited]

        if not choices:
            return None
        
        nextNode = random.choice(choices)
        route.append(nextNode)

        #saveToFile("Current Node: " + currentNode + " -> Choices: " + str(choices) + " | Chosen Node: " + nextNode + " | Route: " + str(route))

    return route

# Takes in a graph and a route
# Returns cost of traversal
def fitness(graph, route):
    cost = 0
    #print(route)
    for i in range(len(route) - 1):
        currentNode = route[i]
        nextNode = route[i+1]
        cost += graph[currentNode][nextNode]
    return cost

# Takes in a population
# Returns the tuple containing the best route along with its cost
def findBest(population):
    best = list(population)[0]
    for route in population:
        if route[1] < best[1]:
            best = route
    
    return best

# Takes in a population size, a graph and max attempts
# Returns a population of routes through the graph,
#     will try to reach the population size until it reaches max attempts
def generatePopulation(populationSize, graph, maxAttempts):
    population = []
    routes = set()
    iteration = 0
    while len(population) < populationSize:
        if len(population) == populationSize or iteration == maxAttempts:
            break

        route = generateRoute(graph, start, finish)

        if route is not None and tuple(route) not in routes:
            population.append((route, fitness(graph, route)))
            routes.add(tuple(route))

        iteration += 1

    return population

# Takes in a route and a graph
# Returns True if the route exists
def validateRoute(route, graph):
    for i in range(len(route) - 1):
        currentNode = route[i]
        nextNode = route[i+1]
        if nextNode not in graph[currentNode]:
            return False
        
    return True

# Takes in a route and a chance of mutation
# Returns mutated route
def mutateRoute(graph, route, chance):
    while True:
        for i in range(1, len(route) - 1):
            randInt = random.randint(0, 100)
            currentNode = route[i]
            previousNode = route[i - 1]
            nextNode = route[i + 1]
            finish = route[-1]

            """ saveToFile("In mutateRoute():")
            saveToFile("    index: " + str(i) + " of " + str(len(route) - 1))
            saveToFile("    route: " + str(route))
            saveToFile("    currentNode: " + currentNode)
            saveToFile("    previousNode: " + previousNode) """

            if randInt <= chance*100 and currentNode is not finish:
                availableNodes = [node for node in graph[previousNode] if node not in route and nextNode in graph[node]]

                #saveToFile("    availableNodes: " + str(availableNodes))

                if len(availableNodes) == 0:
                    continue
                else:
                    mutatedNode = random.choice(availableNodes)
                    route[i] = mutatedNode

        #saveToFile('')

        if validateRoute(route, graph):
            break

        print("Not valid")

    return route

def mutatePopulation(population, graph, chance):
    mutatedPopulation = []
    for tuple in population:
        route = tuple[0]
        mutated = mutateRoute(graph, route, chance)
        mutatedFitness = fitness(graph, mutated)
        currentFitness = fitness(graph, route)
        if mutatedFitness < currentFitness:
            mutatedPopulation.append((mutated, mutatedFitness))
        else:
            mutatedPopulation.append(tuple)

    return mutatedPopulation


import networkx as nx
import matplotlib.pyplot as plt
import os

os.system('cls')

file = "Log.txt"
if os.path.exists(file):
    os.remove(file)

start = '1'
finish = '50'
start = input("Choose starting Node: ").upper()
finish = input("Choose finishing Node: ").upper()
runGraph = graph5

population = generatePopulation(10, runGraph, 1000)

if len(population) == 0:
    print(">Route not found.")
else:
    previousBest = findBest(population)
    attempts = 10

    # Define the path you want to highlight (represented as a list of nodes)
    path = previousBest[0]
    print("==================================================")
    while True:
        #print("Population(" + str(len(population)) + "):")
        #print(population)
        
        best = findBest(population)
        print(">Best:")
        print(">" + str(best))
        print("==================================================")

        population = mutatePopulation(population, runGraph, 0.25)
        previousBest = best
        path = best[0]
        
        if best[1] == previousBest[1]:
            attempts -= 1
        else:
            attempts = 10
        
        if attempts == 0:
            break

    print()
    print(">Done!")

    # Create a directed graph
    G = nx.DiGraph(runGraph)

    # Find the edges in the path
    edges_in_path = [(path[i], path[i+1]) for i in range(len(path)-1)]

    # Create a dictionary to store node and edge colors
    colors = {}
    for node in G.nodes():
        if node in path:
            colors[node] = 'green'
        else:
            colors[node] = 'red'
    for edge in G.edges():
        if edge in edges_in_path:
            colors[edge] = 'green'
        else:
            colors[edge] = 'black'

    # Draw the graph with the updated colors
    nx.draw(G, with_labels=True, node_color=[colors[node] for node in G.nodes()], 
            edge_color=[colors[edge] for edge in G.edges()], 
            width=2, font_size=16, font_weight='bold')
    plt.show()

    os.system('cls')