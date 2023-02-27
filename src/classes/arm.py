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
