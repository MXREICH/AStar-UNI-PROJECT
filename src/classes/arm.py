class Arm:
    def __init__(self, free):
        self.free = free

    def __str__(self):
        if self.free:
            return "armfree:true"
        else:
            return "armfree:false"

    def cpy(self):
        return Arm(self.free)

    def put(self, cube1, cube2=None):  # Permet de mettre le cube1 se trouvant dans le bras sur un cube2 donné
        # if not self.free & cube1.held & cube2.free:
        cube1.held = False
        cube1.free = True
        self.free = True
        if cube2 is not None:
            cube1.on = cube2
            cube2.free = False
        else:
            cube1.ontable = True
