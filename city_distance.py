"""
Problem     -   Given the GPS coordinates of 4 arbitrary cities, A, B, C 
                and D, find the shortest flight route between the 4 cities 
                along the surface of the earth if your journey starts at A.

Observation -   This problem appears to be similar to Traveling Sales man problem.
                Twist to this problem is that no return to starting point is required.

Solution    -   This problem will be solved by TSP. Cost of reaching to the satarting 
                point will be set 0
"""
import latlon

# Direction based lat-long to time based lat long
def input_to_coor(coords:list):
    a = coords[0].strip(" ")
    b = coords[1].strip(" ")
    return latlon.string2latlon(a, b, 'S% %H')

def init_graph(ap: list) ->list :
    # Calculate distance b/w the airports
    m = [[ap[i].distance(ap[j]) for j in range(4)] for i in range(4)]
    # Initializing cost to reaching starting point 0
    for i in range(4):
        m[i][0] = 0
    
    return m

symbols = {0:'A', 1:'B', 2:'C', 3:'D'}
answer = []
final_path = []
V = 4
def tsp(graph, v, currPos, n, count, cost, path):
 
    # If last node is reached and it has
    # a link to the starting node i.e
    # the source then keep the minimum
    # value out of the total cost of
    # traversal and "ans"
    # Finally return to check for
    # more possible values
    if (count == n):
        #append cost
        answer.append(cost)
        # append path for cost
        final_path.append(path)
        return
 
    # BACKTRACKING STEP
    # Loop to traverse the adjacency list
    # of currPos node and increasing the count
    # by 1 and cost by graph[currPos][i] value
    for i in range(n):
        if (v[i] == False and graph[currPos][i]):
             
            # Mark as visited
            v[i] = True
            tsp(graph, v, i, n, count + 1,
                cost + graph[currPos][i], path + [symbols[i]])
             
            # Mark ith node as unvisited
            v[i] = False

def main() -> None:
    airports = [input_to_coor(input("City A: ").split(",")), input_to_coor(input("City B: ").split(",")), input_to_coor(input("City C: ").split(",")), input_to_coor(input("City D: ").split(","))]
    graph = init_graph(airports)
    # Boolean array to check if a node
    # has been visited or not
    v = [False for i in range(4)]
    # Mark 0th node as visited
    v[0] = True
    tsp(graph, v, 0, 4, 1, 0, ['A'])
    mn = 0
    for i in range(4):
        if answer[mn] > answer[i]:
            mn = i
    
    print(final_path[mn][0], end = " ")
    for i in range(1,4):
        print(f"to {final_path[mn][i]}", end = " ")
    
  
if __name__=="__main__":
    main()