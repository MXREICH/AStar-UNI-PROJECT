from src.classes.cube import Cube
from src.classes.arm import Arm


class HNode:
    def __init__(self, cube_array: list[Cube], arm: Arm, heuristic_value, cost_value, parent, children):
        self.cube_array = cube_array
        self.arm = arm
        self.heuristic_value = heuristic_value
        self.cost_value = cost_value
        self.parent = parent
        self.children = children

    def get_cube(self, name):
        for x in self.cube_array:
            if x.name == name:
                return x
        raise Exception("Cube introuvable")

    def arm_put(self, cube, cube2=None):  # Permet de mettre le cube1 se trouvant dans le bras sur un cube2 donné
        new_cube = self.get_cube(cube.name)
        new_cube.held = False
        new_cube.free = True
        self.arm.free = True
        if cube2 is not None:
            new_cube2 = self.get_cube(cube2.name)
            new_cube.on = new_cube2
            new_cube2.free = False
        else:
            new_cube.ontable = True

    def arm_hold(self, cube, cube2=None):
        new_cube = self.get_cube(cube.name)
        new_cube.free = False
        new_cube.held = True
        new_cube.ontable = False
        self.arm.free = False
        if cube2 is not None:
            new_cube2 = self.get_cube(cube2.name)
            new_cube.on = None
            new_cube2.free = True

    def birth(self):
        cubes = []
        for x in self.cube_array:
            cubes.append(x.cpy())
        return HNode(cubes, self.arm.cpy(), self.heuristic_value, self.cost_value, self, [])

    def __hash__(self):
        return hash((''.join((map(str, self.cube_array))), self.arm))

    def __str__(self):
        st = "NODE ["
        for x in self.cube_array:
            st = st + x.name + "/" + ("table" if x.ontable else ("Arm" if x.held else x.on.name)) + ","
            if x.held:
                st = st + "Arm: " + x.name
        if self.arm.free:
            st = st + "Arm: Empty"

        st = st + "|" + str(self.heuristic_value) + "," + str(self.cost_value) + " ]"
        return st

    def __eq__(self, other):
        if isinstance(other, HNode):
            for x in self.cube_array:
                if x not in other.cube_array:
                    return False
            t = self.arm == other.arm and self.heuristic_value == other.heuristic_value
            return t
        return NotImplemented

    def __repr__(self):
        return "Node"
