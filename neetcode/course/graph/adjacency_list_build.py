from pprint import pprint

edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

adjList = {}

for src, dst in edges:

    # Initialise both src and dst nodes if not present:
    if src not in adjList:
        adjList[src] = []
    if dst not in adjList:
        adjList[dst] = []

    adjList[src].append(dst)


pprint(adjList)