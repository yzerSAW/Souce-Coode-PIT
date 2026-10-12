# greedy_tsp_cdo.py
# Traveling Salesperson Problem (TSP) using Nearest Neighbor Algorithm

locations = {
    'A': 'City Hall of Cagayan de Oro',
    'B': 'Gaston Park',
    'C': 'Plaza Divisoria',
    'D': 'Ayala Malls Centrio',
    'E': 'Limketkai Center',
}

# Distance matrix synchronized for a total of 6.90 km (in kilometers)
distances = {
    'A': {'A': 0.0, 'B': 0.45, 'C': 0.55, 'D': 1.80, 'E': 3.00},
    'B': {'A': 0.45, 'B': 0.0, 'C': 0.60, 'D': 1.90, 'E': 2.80},
    'C': {'A': 0.55, 'B': 0.60, 'C': 0.0, 'D': 1.40, 'E': 2.10},
    'D': {'A': 1.80, 'B': 1.90, 'C': 1.40, 'D': 0.0, 'E': 1.45},
    'E': {'A': 3.00, 'B': 2.80, 'C': 2.10, 'D': 1.45, 'E': 0.0},
}


def validate_data():
  """Checks if matrix has all locations and is symmetric."""
  for node1 in locations:
    for node2 in locations:
      if abs(distances[node1][node2] - distances[node2][node1]) > 1e-5:
        return False
  return True


def nearest_neighbor_tsp(start_node):
  if not validate_data():
    print('Error: Invalid or asymmetric distance matrix!')
    return None, [], []

  current = start_node
  visited = [current]
  total_distance = 0.0
  legs = []

  print(f'START: {current} - {locations[current]}\n')
  print('ROUTE STEPS:')

  while len(visited) < len(locations):
    unvisited = [node for node in locations if node not in visited]
    # Find the nearest unvisited neighbor
    next_node = min(unvisited, key=lambda node: distances[current][node])
    step_dist = distances[current][next_node]

    legs.append((current, next_node, step_dist))
    total_distance += step_dist

    print(
        f'{current} ({locations[current]}) -> {next_node}'
        f' ({locations[next_node]}): {step_dist} km'
    )

    visited.append(next_node)
    current = next_node

  # Return to start node (A)
  return_dist = distances[current][start_node]
  legs.append((current, start_node, return_dist))
  total_distance += return_dist

  print(
      f'{current} ({locations[current]}) -> {start_node}'
      f' ({locations[start_node]}): {return_dist} km (return to start)'
  )

  route = visited + [start_node]
  return route, total_distance, legs


if __name__ == '__main__':
  start_vertex = 'A'
  route, total_dist, legs = nearest_neighbor_tsp(start_vertex)

  print('\nFINAL ROUTE: ' + ' -> '.join(route))
  print(f'\nTOTAL DISTANCE: {total_dist:.2f} km')

  # Verification checks
  all_visited_once = (
      set(route[:-1]) == set(locations.keys())
      and len(route[:-1]) == len(locations)
  )
  returned_home = route[-1] == start_vertex
  recalculated_sum = sum(leg[2] for leg in legs)

  print(f'Each required location visited exactly once: {all_visited_once}')
  print(f'Returned to starting location: {returned_home}')
  print(f'Recalculated from route legs: {recalculated_sum:.2f} km')