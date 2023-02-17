class Arm:
    def __init__(self):
        self.free = True

    def hold(self, cube):  # Permet de tenir un cube, s'il se trouve sur la table.
        if self.free & cube.free & cube.ontable:
            cube.free = False
            cube.held = True
            cube.ontable = False
            self.free = False

    def hold(self, cube1, cube2):  # Permet de tenir un cube, si il est libre et qu'il se trouve un autre ou non.
        if self.free & cube1.on == cube2 & cube1.free:
            cube1.free = False
            cube1.held = True
            self.free = False
            cube1.on != cube2

    def put(self, cube1, cube2):  # Permet de mettre le cube1 se trouvant dans le bras sur un cube2 donné
        if not self.free & cube1.held & cube2.free:
            cube2.free = False
            cube1.free = True
            self.free = True
            cube1.on = cube2
            cube1.held = False

    def put(self, cube):  # Permet de mettre le cube qui se trouve dans le bras sur la table
        if not self.free & cube.held:
            self.free = True
            cube.free = True
            cube.ontable = True
            cube.held = False
