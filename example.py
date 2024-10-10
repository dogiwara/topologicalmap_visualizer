import networkx as nx
import argparse
from modules import TopologicalMap

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--topological_map_path", type=str, default="path/to/topological_map.pkl")
args = parser.parse_args()

# Load the topological map
topological_map = TopologicalMap.load(args.topological_map_path)

print("number of nodes")
print(len(topological_map.nodes))

print("get edges")
print(topological_map.graph.edges(data=True))

print("get connected edges from node 0")
print(topological_map.graph.edges(0))

print("get connected edges and weights from node 0")
print(topological_map.graph.edges(0, data=True))