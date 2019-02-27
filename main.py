# Data source: https://www.whatdotheyknow.com/request/distance_between_adjacent_underg
# Columns deleted from this spreadsheet prior to use (Length distances, Tube Line info and Zone number)

import numpy as np 
import pandas as pd 
import scipy.sparse as sparse


class Tubemap:
    """A network of all stations as vertices, and time travelled between them as edges. """  

    def create(connections = 'london.connections.csv', stations = 'london.stations.csv' ):
        """Creates the travel network object requried for further methods """

        #Load csv file of interstation travel times, with default of the London Tube Map file 
        traveltime_df = pd.read_csv(connections)
        
        #Parse relevant columns to new array objects: start station, finish station, time to travel between them. 
        start, finish, time = [], [], []
        start = traveltime_df['station1'].values.ravel() 
        finish = traveltime_df['station2'].values.ravel()
        time = traveltime_df['time'].values.ravel()

        #Create a sparse matrix of all tube connections
        tube_map = sparse.coo_matrix((time, (start, finish)), shape=(300,304))

        #Create a dictionary to match each node/station number to station name from stations database
        stations_df = pd.read_csv(stations)
        station_dict = dict(zip(stations_df.id, stations_df.name))

    def min_pos(graph):
        """ Given a graph will return (min value in graph, initial station, arrival station) """
        min = graph.data.argmin()
        minval = graph.data[min]
        minrow = graph.row[min]
        mincol = graph.col[min]
        return (minval, minrow, mincol)


print(min_pos(tube_map))

#PRIMMS ALGORITHM
#def mst_primms:

#     #KRUSKALS ALGORITHM
#     def mst_kruskals()


# class journey:
# #return journey length 
# #start and end points

# class shortest_path: 
#     #inherits jouney

# class travelling_salesman: 
#     #inherits journey
#     #APPROXIMATION ALGORITHM FOR TSP
#     def tsp_approx()



#Functionality to implement
## SIMPLE ALGORITHMS
# - Shortest path between two stations - Dijkstra's algorithm 
# - Travelling Salesman
#  - - Approximation algorithm using Minimum Spanning Tree of network, with choice of Primm's or Kruskal's algorithms
## METAHEURISTICS
#  - - Random descent
#  - - Simulated annealing
#  - - Steepest descent
#  - - Tabu method
#classes - minimum spanning tree, shortest path (between two objects or round)



# #DIJKSTRAS ALGORITHM - SHORTEST PATH
# def dijkstras()

# #RANDOM DESCENT
# def random_descent()


# #









