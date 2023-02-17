class Arm:
    def __init__(self):
        self.free = 1

    def hold(self, cube): # Permet de tenir un cube, s'il se trouve sur un autre ou non.
        if self.free & cube.free & cube.ontable:
            cube.free = 0
            cube.held = 1
            cube.ontable = 0

    def hold(self,cube1,cube2):


    def put(self,cube1,cube2): # Permet de mettre le cube1 se trouvant dans le bras sur un cube2 donné

    def put(self,cube): # Permet de mettre le cube qui se trouve dans le bras sur la table

