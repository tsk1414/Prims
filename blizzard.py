import sys
import heapq

num_towns = int(input("Enter number of towns: "))
town_list = []

for i in range(num_towns):
    town_list.append(input("Town: "))
    
num_roads = int(input("Enter number of roads: "))

all_edges = {}

for i in range(num_roads):
    edge = input()
    
    edgeList = edge.split(',')
    town_A = edgeList[0].strip()
    town_B = edgeList[1].strip()
    weight = int(edgeList[2].strip())
    
    temp_list = []
    temp_list.append(town_A)
    temp_list.append(town_B)
    a_tuple = tuple(temp_list)
    all_edges[a_tuple] = weight

key_edge = list(all_edges.keys())
val_weight = list(all_edges.values())


mst = []

start = town_list[0]

minpq = []
minpq_edge = {}

#adding the first node and all its neighbors
for a_edge in key_edge:
    if start in a_edge:
        #append weight to pri queue
        minpq.append(all_edges[a_edge])
        #append edge to pri queue
        minpq_edge[a_edge] = all_edges[a_edge]
    
heapq.heapify(minpq)

total = 0
townsList = []
while len(mst) < num_towns - 1:
    tempkey_list = list(minpq_edge.keys())
    tempval_list = list(minpq_edge.values())
    
    #Pop the lowest weight node N from Q.
    min_weight = heapq.heappop(minpq)
    min_edge =  tempkey_list[tempval_list.index(min_weight)]
  
    minpq_edge.pop(min_edge, None)
    

    key_list = list(minpq_edge.keys())
 
    #If N is not already in MST, add it to MST and add all its neighbors 
    #(that aren’t already in MST) to Q.
    
    town_A = min_edge[0]
    town_B = min_edge[1]
    
    is_new = False
    
    
    if town_A not in townsList:
        townsList.append(town_A)
        is_new = True
    if town_B not in townsList:
        townsList.append(town_B)
        is_new = True
    if is_new is True:
        mst.append(min_edge)


        total += min_weight

        for a_edge in key_edge:

            if town_A in a_edge or town_B in a_edge:
                    if a_edge not in mst:
                        #print("not in mst")
                        if a_edge not in key_list:
                            #print("not in keylist")
                            heapq.heappush(minpq,all_edges[a_edge]) 
                            minpq_edge[a_edge] = all_edges[a_edge]

print (total)

    
    