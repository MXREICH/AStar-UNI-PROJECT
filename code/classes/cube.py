class Cube:
    def __init__(self, on, free, ontable, held, name):
        self.held = held
        self.on = on
        self.free = free
        self.ontable = ontable
        self.name = name

    def __hash__(self):
        return hash((self.held, self.on, self.free, self.ontable))

    def __str__(self):
        if self.on is not None:
            return "[ CUBE " + self.name + " ] held:" + str(self.held) + " on:" + self.on.name + " free:" + str(
                self.free)
        else:
            return "[ CUBE " + self.name + " ] held:" + str(self.held) + " on:table" + " free:" + str(
                self.free)

    def __eq__(self, other):
        if isinstance(other, Cube):
            return self.held == other.held and self.on == other.on and self.free == other.free and self.ontable == other.ontable
        return NotImplemented
