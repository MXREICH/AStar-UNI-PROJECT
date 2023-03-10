from src.classes.cube import Cube
from src.classes.arm import Arm


def eq_node(node1, node2): # la fonction compare directement par valeur les états des cubes d'un node
    for x, y in zip(node1.cube_array, node2.cube_array):
        if x.free != y.free or x.held != y.held or x.ontable != y.ontable or (x.on is None and y.on is not None) or (
                x.on is not None and y.on is None):
            return False
        if not (x.on is None and y.on is None) and x.on.name != y.on.name:
            return False
    return True


def find_arr(node_arr, node): # trouve le noeud `node` dans `node_arr`
    for node_i in node_arr:
        if eq_node(node_i, node):
            return node_i
    return None


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

    def arm_put(self, cube, cube2=None):  # Gestion des deux opérateurs en un seul grâce au passage de "None" si
        # le cube2 n'est pas rempli lors de l'appel de fonction
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

    def arm_hold(self, cube, cube2=None):  # Gestion des deux opérateurs en un seul grâce au passage de "None" si
        # le cube2 n'est pas rempli lors de l'appel de fonction
        new_cube = self.get_cube(cube.name)
        new_cube.free = False
        new_cube.held = True
        new_cube.ontable = False
        self.arm.free = False
        if cube2 is not None:
            new_cube2 = self.get_cube(cube2.name)
            new_cube.on = None
            new_cube2.free = True

    def birth(self):  # créer une deepcopy() des valeurs d'un node, puis l'associe en tant que parent avec self.
        cubes = []
        for x in self.cube_array:
            cubes.append(x.cpy())
        return HNode(cubes, self.arm.cpy(), self.heuristic_value, self.cost_value, self, [])

    def __hash__(self):
        return hash((''.join((map(str, self.cube_array))), self.arm))

    def __str__(self):
        st = ""
        for x in self.cube_array:
            st = st + x.name + "/" + ("table" if x.ontable else ("Arm" if x.held else x.on.name)) + "\n"
        if self.arm.free:
            st = st + "Arm: Empty | "
        st = st + "h=" + str(self.heuristic_value) + ", g=" + str(self.cost_value)
        return st

    def __eq__(self, other):
        if isinstance(other, HNode):
            for x in self.cube_array:
                if x not in other.cube_array:
                    return False
            t = self.arm == other.arm and self.heuristic_value == other.heuristic_value  # On ne compare que ce qui
            # caractérise un noeud dans la situation réelle
            return t
        return NotImplemented

    def __repr__(self):
        return "Node"
