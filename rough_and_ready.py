import numpy as np 
import pandas as pd 
import scipy.sparse as sparse

#Load csv file of interstation travel times, with default of the London Tube Map file 
traveltime_df = pd.read_csv('london.connections.csv')

# relevant columns to new array objects: start station, finish station, time to travel between them. 
start, finish, time = [], [], []
start = traveltime_df['station1'].values.ravel() 
finish = traveltime_df['station2'].values.ravel()
time = traveltime_df['time'].values.ravel()

#Create a CSR (compressed sparse row) matrix of all tube connections
tube_map = sparse.csr_matrix((time, (start, finish)), shape=(300,304))

#Create a dictionary to match each node/station number to station name from stations database
stations_df = pd.read_csv('london.stations.csv')
station_dict = dict(zip(stations_df.id, stations_df.name))


def min_pos(graph):
    """ Given a graph will return (min value in graph, initial station, arrival station) """

    min = graph.data.argmin() #location of min value in the graph
    minval = graph.data[min] #rminimum value
    minrow = graph.row[min] #row of minimum value
    mincol = graph.col[min] #column of minimum value
    return (minval, minrow, mincol)

def min_distance(graph, start)
    """ Given a graph and a starting station will return the shortest journey that can be taken from that station """
    
# def primms(graph):
#     """ Finds a minimum spanning tree using Primms algorithm. """
    

    
print(tube_map.toarray())

