import tsplib95 # pyright: ignore[reportMissingImports]

#Load the problem file
task = tsplib95.load('berlin52.tsp')

#View the files contents
print("--------------------------------------------------------------------------------------------------------------------")
print("[NAME]: " + str(task.name))
print("[DIMENSION]: " + str(task.dimension))
print("[WEIGHT_TYPE]: " + str(task.edge_weight_type))
print("[WEIGHT_FORMAT]: " + str(task.edge_weight_format))
print("[NODE_TYPE]: " + str(task.node_coord_type))
print("[NODE_DIPLAY]: " + str(task.display_data_type))
print("--------------------------------------------------------------------------------------------------------------------\n")

'''
coords = task.node_coords

#Find node weight test
weight = task.get_weight(1, 2)
print("Weight(1, 2) - " + str(weight))

coords = task.node_coords

# Access specific coordinate test
node_1_x, node_1_y = coords[1]
print("X - " + str(node_1_x))
print("Y - " + str(node_1_y))
'''

#Functions
def closest_path(node, size, map):
    current = -1
    shortest = -1
    i = 1
    while(i <= 52):
        if(i != node):
            current = map.get_weight(node, i)
            if(shortest == -1):
                shortest = current
            elif(current < shortest):
                shortest = current
        i+=1
    
    return shortest


#Main
coords = task.node_coords
print(closest_path(1, 52, task))