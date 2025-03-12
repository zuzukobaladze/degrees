# Degrees Solution

## Overview
This solution implements a program that finds the shortest path between any two actors in Hollywood using the "Six Degrees of Kevin Bacon" concept. The implementation uses a breadth-first search (BFS) algorithm to find the shortest connection between actors through movies they've starred in together.

## Implementation Details

### Core Function: `shortest_path`

```python
def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target using breadth-first search.
    """
    if source == target:
        return []
    
    start = Node(state=source, parent=None, action=None)
    frontier = QueueFrontier()
    frontier.add(start)
    explored = set()

    while not frontier.empty():
        current_node = frontier.remove()
        explored.add(current_node.state)
        
        for movie_id, person_id in neighbors_for_person(current_node.state):
            if person_id == target:
                path = [(movie_id, person_id)]
                while current_node.parent is not None:
                    path.append((current_node.action, current_node.state))
                    current_node = current_node.parent
                path.reverse()
                return path
                
            if person_id not in explored and not frontier.contains_state(person_id):
                child = Node(state=person_id, parent=current_node, action=movie_id)
                frontier.add(child)
    
    return None
```

### Key Components

1. **Node Class**
   - Stores the current state (person_id)
   - Keeps track of the parent node
   - Records the action (movie_id) that led to this state

2. **QueueFrontier**
   - Implements a FIFO queue for BFS
   - Ensures we find the shortest path first

### Algorithm Breakdown

1. **Initialization**
   - Create starting node with source actor
   - Initialize empty frontier queue and explored set
   - Add start node to frontier

2. **Search Process**
   - While frontier is not empty:
     1. Remove next node from frontier
     2. Add current state to explored set
     3. Get all neighbors (connected actors) through movies
     4. For each neighbor:
        - If target found, reconstruct and return path
        - If unexplored, add to frontier

3. **Path Reconstruction**
   - When target is found, build path by:
     1. Starting at target node
     2. Following parent references back to source
     3. Collecting (movie_id, person_id) pairs
     4. Reversing the path to get source-to-target order

### Optimizations

1. **Early Termination**
   - Returns empty list if source equals target
   - Returns path immediately when target is found

2. **Memory Efficiency**
   - Uses set for O(1) lookup in explored states
   - Only stores necessary path information

3. **Search Efficiency**
   - Checks target condition during neighbor exploration
   - Avoids adding already explored or frontier states

### Time and Space Complexity

- **Time Complexity**: O(V + E)
  - V: number of actors (vertices)
  - E: number of connections through movies (edges)

- **Space Complexity**: O(V)
  - Stores explored set and frontier
  - Keeps track of path information

## Usage Example

```python
# Find path between Emma Watson and Jennifer Lawrence
path = shortest_path("emma_watson_id", "jennifer_lawrence_id")

# Output might look like:
# 3 degrees of separation.
# 1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
# 2: Brendan Gleeson and Michael Fassbender starred in Trespass Against Us
# 3: Michael Fassbender and Jennifer Lawrence starred in X-Men: First Class
```

## Edge Cases Handled

1. **Same Actor**: Returns empty list when source and target are the same
2. **No Connection**: Returns None when no path exists
3. **Direct Connection**: Correctly identifies when actors have worked together directly
4. **Multiple Paths**: Returns first (shortest) path found due to BFS nature

## Data Structure Dependencies

- Uses `Node` class for state management
- Uses `QueueFrontier` for BFS implementation
- Requires access to:
  - `people` dictionary (person_id → person data)
  - `movies` dictionary (movie_id → movie data)
  - `neighbors_for_person` function for finding connections