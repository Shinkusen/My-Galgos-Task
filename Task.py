import tsplib95 # pyright: ignore[reportMissingImports]

#Load the problem file
task = tsplib95.load('berlin52.tsp')

#View the files contents
print("[NAME]: " + str(task.name))
print("[DIMENSION]: " + str(task.dimension))
print("[WEIGHT_TYPE]: " + str(task.edge_weight_type))
print("[WEIGHT_FORMAT]: " + str(task.edge_weight_format))
print("[NODE_TYPE]: " + str(task.node_coord_type))
print("[NODE_DIPLAY]: " + str(task.display_data_type))
print("[COORDS]: " + str(task.node_coords))
print("----------------------------------------------------------------------------------------------------------------------------\n")

#Find node weight test
weight = task.get_weight(1, 2)
print(f"Weight between node 1 and 2: {weight}")