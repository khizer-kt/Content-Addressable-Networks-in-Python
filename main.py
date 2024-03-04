import hashlib
import math
import matplotlib.pyplot as plt
import random

class CANNode:
    def __init__(self, id):
        self.id = id
        self.position = [0.0, 0.0]  # Origin
        self.neighbours = []

    def __repr__(self):
        return f"Node {self.id} at position {self.position}"

class ContentAddressableNetwork:
    def __init__(self):
        self.nodes = []

    def distance(self, pos1, pos2):
        return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

    def hash(self, data):
        return int(hashlib.sha1(data.encode()).hexdigest(), 16)

    def add_node(self, node):
        self.nodes.append(node)
        self.update_neighbours()

    def remove_node(self, node_id):
        self.nodes = [n for n in self.nodes if n.id != node_id]
        for n in self.nodes:
            n.neighbours = [neighbour for neighbour in n.neighbours if neighbour.id != node_id]

    def get_closest_node(self, data):
        hash_value = self.hash(data)
        min_distance = float('inf')
        closest_node = None

        for node in self.nodes:
            d = self.distance(node.position, [hash_value, hash_value])
            if d < min_distance:
                min_distance = d
                closest_node = node

        return closest_node

    def update_neighbours(self):
        for node in self.nodes:
            node.neighbours = []
            for other_node in self.nodes:
                if other_node != node:
                    node.neighbours.append(other_node)

    def display_network(self):
        print("Content Addressable Network:")
        for node in self.nodes:
            print(node)

    def visualize_network(self):
        plt.figure(figsize=(8, 8))
        for node in self.nodes:
            plt.plot(node.position[0], node.position[1], 'bo')
            for neighbour in node.neighbours:
                plt.plot([node.position[0], neighbour.position[0]], [node.position[1], neighbour.position[1]], 'r-')
        plt.title("Content Addressable Network")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.show()

    def nearest_neighbour_routing(self, data):
        closest_node = self.get_closest_node(data)
        print(f"Data '{data}' is routed to closest node: {closest_node}")

can = ContentAddressableNetwork()

for i in range(5):
    node = CANNode(i)
    node.position = [round(random.random(), 2), round(random.random(), 2)]
    can.add_node(node)

can.display_network()
can.visualize_network()

data = "example_data"
can.nearest_neighbour_routing(data)