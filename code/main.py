import anytree

from classes.cube import Cube
from classes.heap import Node
from classes.arm import Arm

if __name__ == '__main__':
    A = Cube(0, True, False, True)
    B = Cube(0, True, False, True)
    Arm = Arm()
    NodeA = Node([A,B], Arm, 0, 0)
    NodeB = Node([A,B], Arm, 0, 0)
    NodeC = Node([A,B], Arm, 1, 0)
    print("A:",hash(NodeA), "B:", hash(NodeB), "C:", hash(NodeC))