# Path-Finder
Personal project testing out implementation of network algorithms on the London Tube Map. 

### File layout
Testing candidate solutions in roughandready.py before commiting these to main.py, which will have appropriate class/function structure. 

## Progress
- Imported tube map into a matrix
- Set-up dictionary for name references
- Function returning shortest journey in a graph
- TODO NEXT: Function returning shortest journey given fixed start station


## CSV Map Source
The data used for this project is freely available here: https://commons.wikimedia.org/wiki/London_Underground_geographic_maps/CSV

## Planned implementation
Using scipy sparse matrices (time/memory saver compared to multiple adjacency lists) to store a sparse adjacency matrix which represents  the tubemap as an edge-weighted, non-directional, connected network. Stations are represented by numerical indices, and so a dictionary is used to hold the key/value pairs of station numerical index to name. 

### Minimum spanning trees
- Exploring implementation of Primms and Kruskal's algorithms to produce a minimum spanning tree (MST). 

### Finding shortest journey
- This will involve implementing Dijkstra's algorithm for shortest path to minimise the journey between any two stations.

### Travelling Salesman
- Visiting all stations in opimum length of time. 
-- Implement candidate solution using MST, random descent, steepest descent, simulated annealing, tabu. 
