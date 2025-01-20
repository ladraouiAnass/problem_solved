import pandas as pd
from .apps import global_config
from .models import ROUTES


def get_graph():
    print("here you call the get_graph function")
    routes_list = ROUTES.get_routes()
    
    planets = [sublist[0] for sublist in routes_list]
    planets.extend([sublist[1] for sublist in routes_list])
    planets = set(planets)
    planets = list(planets)
    
    matrix = [[0 for _ in range(len(planets))] for _ in range(len(planets))]
    
    graph = {}
    for route in routes_list:
        if route[0] in list(graph.keys()):
            graph[route[0]][route[1]] = route[2]
        else:
            graph[route[0]] = {route[1]:route[2]}
    
    for planet in list(graph.keys()):
        i = planets.index(planet)
        for dest in list(graph[planet].keys()):
            j = planets.index(dest)
            matrix[i][j] = graph[planet][dest]
            
    return graph, matrix





def proba(graph, current, end, day, autonomy, k, max_autonomy, countdown, bounty_hunters):
    for i in range(len(bounty_hunters)):
        if  bounty_hunters[i]["planet"]==current and bounty_hunters[i]["day"]==day:
            k+=1
            break
    if autonomy==0:
        autonomy = max_autonomy
        day+=1
        for i in range(len(bounty_hunters)):
            if  bounty_hunters[i]["planet"]==current and bounty_hunters[i]["day"]==day:
                k+=1
                break
    if current == end :
        if k<0:
            return 0
        else:
            risk = 0
            for q in range(k):
                risk+=(9**q)/(10**(q+1))
            return risk
    possibilities = []
    for dest in list(graph[current].keys()):
        if dest in list(graph.keys()):
           if day+graph[current][dest]<=countdown and autonomy-graph[current][dest] >= 0:
                possibilities.append( proba(graph, dest,end, day+graph[current][dest], autonomy-graph[current][dest], k, max_autonomy, countdown, bounty_hunters) )
           else:
             possibilities.append(1)
             
        else:
            if dest == end and day+graph[current][dest]<=countdown and autonomy-graph[current][dest] >= 0:
                possibilities.append(proba(graph, dest,end, day+graph[current][dest], autonomy-graph[current][dest], k, max_autonomy, countdown, bounty_hunters))
            else:
                possibilities.append(1)  
            
    return min(possibilities)

    
    