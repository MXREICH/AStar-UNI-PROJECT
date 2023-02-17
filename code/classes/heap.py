class Node:
    def __init__(self, cube_array, arm, heuristic_value, cost_value):
        self.cube_array = cube_array
        self.arm = arm
        self.heuristic_value = heuristic_value
        self.cost_value = cost_value

class Heap:

