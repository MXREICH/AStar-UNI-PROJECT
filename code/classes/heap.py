class Node:
    def __init__(self, cube_array, arm, heuristic_value, cost_value, parent, children):
        self.cube_array = cube_array
        self.arm = arm
        self.heuristic_value = heuristic_value
        self.cost_value = cost_value
        self.parent = parent
        self.children = children

    def __hash__(self):
        return hash((''.join((map(str, self.cube_array))), self.arm, self.heuristic_value, self.cost_value))

    