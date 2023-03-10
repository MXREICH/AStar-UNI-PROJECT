from anytree import Node
from anytree.exporter import DotExporter

from classes.astar import astar, heuristic2
from classes.astar import heuristic1
from classes.astar import realcost1
from classes.cube import Cube
from classes.heap import HNode
from classes.arm import Arm


def path_to_tree(hnode, ref):
    new_node = Node(str(hnode))
    ref[str(hnode)] = new_node
    if hnode.parent is not None:
        new_node.parent = ref[str(hnode.parent)]
    if len(hnode.children) == 0:
        return
    else:
        for child in hnode.children:
            path_to_tree(child, ref)


if __name__ == '__main__':
    A = Cube(None, False, True, False, "A")
    B = Cube(A, False, False, False, "B")
    C = Cube(B, True, False, False, "C")
    Arm = Arm(True)

    cubes = [A, B, C]
    children = []

    startnode = HNode(cubes, Arm, 10, 0, None, children)

    A = Cube(B, True, False, False, "A")
    B = Cube(C, False, False, False, "B")
    C = Cube(None, False, True, False, "C")

    cubes = [A, B, C]
    Arm2 = Arm
    goalnode = HNode(cubes, Arm2, 0, 0, None, children)

    nodes = []
    nodes = astar(heuristic1, realcost1, startnode, goalnode)
    ref = dict()
    path_to_tree(startnode, ref)
    DotExporter(ref[str(startnode)]).to_picture("test2.png")