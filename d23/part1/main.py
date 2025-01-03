def explore(graph, visited, found):
  for node in sorted(graph[visited[-1]]):
    if node != visited[-1]:
      if len(visited) != 2:
        explore(graph, visited + [node], found)
      elif visited[0] in graph[node] and (visited[0][0] == "t" or visited[1][0] == "t" or node[0] == "t"):
        found.add(tuple(sorted(visited + [node])))

def main():
  with open("input.txt", "r") as file:
    graph = {}
    for line in file:
      nodes = line.strip().split("-")
      if nodes[0] in graph:
        graph[nodes[0]].append(nodes[1])
      else:
        graph[nodes[0]] = [nodes[1]]
      if nodes[1] in graph:
        graph[nodes[1]].append(nodes[0])
      else:
        graph[nodes[1]] = [nodes[0]]


  # print(graph)
  groups = set()
  for node in sorted(graph):
    explore(graph, [node], groups)

  for g in sorted(groups):
    print(",".join(g))

  print("Count of group:", len(groups))


if __name__ == "__main__":
  main()