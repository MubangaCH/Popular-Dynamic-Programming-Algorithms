
import queue
import sys




def Dijkstra(adj, cost, departure_city, Arrival_city):
    
    dist = [float('inf')] * len(adj) #initialize a list to store maximum distances (inifity) from start to each city
    dist[departure_city] = 0 # give the start city the smallest distance
    q = queue.PriorityQueue()
    

    q.put((departure_city,dist[departure_city])) # add start city to queue double brackets gets both start and distance
    
    
        
    while not q.empty():
        
        u=q.get() #gets 0 or the number if no double brackets, start city is first in queue since it has smallest distance
        current_city = u[0]   
        
        for next_city in adj[current_city]: #traverse through graph to get to next city
            
               
            next_city_index = adj[current_city].index(next_city) #get index of neighbor its needed because cost list is a separate from adjacency list
           
      
            if dist[next_city] > dist[current_city] + cost[current_city][next_city_index]:  #check if distance to next city is large
                
                dist[next_city] = dist[current_city] + cost[current_city][next_city_index] # relax the distance, or replace with shorter distance
                
                
                q.put((next_city,dist[next_city]))   #queue new distance of the next city      
        
       
    if dist[Arrival_city] == float('inf'): # check if destination was reachable
        return -1
        
    return dist[Arrival_city]
        

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    departure_city, Arrival_city = data[0] - 1, data[1] - 1
    
   
    print(Dijkstra(adj, cost, departure_city, Arrival_city))



