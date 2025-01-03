def explore(graph, visited, found):
  if tuple(sorted(visited)) in found:
    return
  found.add(tuple(sorted(visited)))
  for node in graph[visited[-1]]:
    if node not in visited and set(visited) <= set(graph[node]):
      explore(graph, visited + [node], found)


def main():
  with open("input.txt", "r") as file:
    graph = {}
    for line in file:
      nodes = line.strip().split("-")
      graph[nodes[0]] = sorted(graph.get(nodes[0], []) + [nodes[1]])
      graph[nodes[1]] = sorted(graph.get(nodes[1], []) + [nodes[0]])

  groups = set()
  for node in sorted(graph):
    explore(graph, [node], groups)

  result = ""
  for g in sorted(groups):
    tmp = ",".join(g)
    if len(result) < len(tmp):
      result = tmp

  print(result)


if __name__ == "__main__":
  main()