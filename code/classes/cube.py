class Cube:
    def __init__(self, on, free, ontable, held):
        self.held = held
        self.on = on
        self.free = free
        self.ontable = ontable

    def __hash__(self):
        return hash((self.held, self.on, self.free, self.ontable))