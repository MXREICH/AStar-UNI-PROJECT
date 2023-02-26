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

    def __str__(self):
        st = "NODE [ "
        for x in self.cube_array:
            st = st + x.name + ","

        st = st + "|" + str(self.heuristic_value) + "," + str(self.cost_value) + " ]"
        return st

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.cube_array == other.cube_array and self.arm == other.arm and self.heuristic_value == other.heuristic_value and self.cost_value == other.cost_value and self.parent == other.parent and self.children == other.children
        return NotImplemented

    def __repr__(self):
        return "Node"
