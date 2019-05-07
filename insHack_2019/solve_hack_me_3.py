import operator

def openFile():
    routes = []
    with open('routes.txt', 'r') as f:
        for line in f:
            data = line.strip().split(',')
            tmp = []
            for d in data:
                tmp.append(d)
            routes.append(tmp)
            tmp = None
    return routes

# Select only the most frequently used node in the routes
def findMostFreq(routes):
    freq_map = {}
    for route in routes:
        for node in route:
            freq_map[node] = freq_map.get(node, 0) + 1
    freq_map = sorted(freq_map.items(), key=operator.itemgetter(1), reverse=True)
    return freq_map[0][0]

# select most frequent,
# find all routes that do not contain bestNode
# Rerun the function with the new set of routes
def genValidRoutes(routes, valid_routes = []):
    bestNode = findMostFreq(routes)
    valid_routes.append(bestNode)

    new_routes = []
    for route in routes:
        if bestNode not in route:
            new_routes.append(route)
    
    if (len(new_routes) == 0):
        print(len(valid_routes))
        print(valid_routes)
    else:
        genValidRoutes(new_routes, list(valid_routes))

genValidRoutes(openFile())