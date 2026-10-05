from queue import PriorityQueue

goal = [[1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]]

def manhattan_distance(state):
    distance = 0
    goal_coords = {}
    for r in range(3):
        for c in range(3):
            goal_coords[goal[r][c]] = (r, c)
            
    for r in range(3):
        for c in range(3):
            val = state[r][c]
            if val != 0:
                target_r, target_c = goal_coords[val]
                distance += abs(r - target_r) + abs(c - target_c)
    return distance

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_children(state):
    x, y = find_blank(state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    children = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            children.append(new_state)
    return children

def astar_manhattan(start):
    pq = PriorityQueue()
    h = manhattan_distance(start)
    pq.put((h, 0, 0, start))
    visited = set()
    counter = 1

    while not pq.empty():
        f, g, _, current = pq.get()
        key = str(current)
        if key in visited:
            continue
        visited.add(key)

        for row in current:
            print(row)
        print("\n")
        if current == goal:
            print("\nGoal State Reached")
            return

        for child in generate_children(current):
            h = manhattan_distance(child)
            new_g = g + 1
            new_f = new_g + h
            pq.put((new_f, new_g, counter, child))
            counter += 1

initial = [[2, 8, 3],
         [1, 6, 4],
         [0, 7, 5]]

astar_manhattan(initial)
