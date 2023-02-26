import anytree
from anytree import Node, RenderTree
from anytree.exporter import DotExporter

from classes.astar import astar
from classes.astar import heuristic1
from classes.astar import realcost1
from classes.cube import Cube
from classes.heap import HNode
from classes.arm import Arm

if __name__ == '__main__':
    A = Cube(None, False, True, False, "A")
    B = Cube(A, False, False, False, "B")
    C = Cube(B, True, False, False, "C")
    Arm = Arm(True)

    cubes = [A, B, C]
    children = []

    startnode = HNode(cubes, Arm, 3, 0, None, children)

    A = Cube(C, True, False, False, "A")
    C = Cube(B, False, False, False, "C")
    B = Cube(None, False, True, False, "B")

    cubes = [A, B, C]
    goalnode = HNode(cubes, Arm, 0, 0, None, children)

    nodes = []
    nodes = astar(heuristic1, realcost1, startnode, goalnode)
    print(nodes)