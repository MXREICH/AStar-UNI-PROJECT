import anytree

from classes.astar import astar
from classes.astar import heuristic1
from classes.astar import realcost1
from classes.cube import Cube
from classes.heap import Node
from classes.arm import Arm

if __name__ == '__main__':
    A = Cube(None, False, True, False, "A")
    B = Cube(A, True, False, False, "B")

    Arm = Arm()

    NodeA = Node([A, B], Arm, 0, 0, None, [])

    A = Cube(B, True, False, False, "A")
    B = Cube(None, False, True, False, "B")
    NodeB = Node([A, B], Arm, 0, 0, None, [])

    print(astar(heuristic1, realcost1, NodeA, NodeB))

