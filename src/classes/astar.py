from arm import Arm
from heap import Node


def heuristic1(currentnode, goalnode):
    n = len(goalnode.cube_array)
    it = 0
    for x, y in zip(goalnode.cube_array, currentnode.cube_array):
        if hash(x) == hash(y):
            it = it + 1
    currentnode.heuristic_value = n - it
    return n - it


def realcost1(currentnode):
    currentnode.cost_value = currentnode.cost_value + 1
    return currentnode.cost_value


def astar(h, g, startnode, goalnode):
    openlist = [startnode]
    closedlist = set()

    while openlist:
        current = min(openlist, key=lambda x: x.cost_value + x.heuristic_value)
        openlist.remove(current)

        if current == goalnode:
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1]

        closedlist.add(current)

        for child in current.children:
            if child in closedlist:
                continue

            tentative_g = current.cost_value + g(current, child)
            if child not in openlist or tentative_g < child.cost_value:
                child.cost_value = tentative_g
                child.parent = current
                if child not in openlist:
                    openlist.append(child)

        for cube in current.cube_array:
            if cube.held:
                for cube2 in current.cube_array:
                    if cube2.free and cube2 != cube:
                        new_cubes = list(current.cube_array)
                        new_arm = Arm()
                        new_arm.hold2(cube, cube2)
                        new_cubes.remove(cube)
                        new_cubes.append(cube)
                        new_node = Node(new_cubes, new_arm, h(new_cubes, goalnode.cube_array), float('inf'), current, [])
                        current.children.append(new_node)

                new_cubes = list(current.cube_array)
                new_arm = Arm()
                new_arm.put(cube)
                new_cubes.remove(cube)
                new_cubes.append(cube)
                new_node = Node(new_cubes, new_arm, h(new_cubes, goalnode.cube_array), float('inf'), current, [])
                current.children.append(new_node)

            elif cube.ontable:
                new_cubes = list(current.cube_array)
                new_arm = Arm()
                new_arm.hold(cube)
                new_cubes.remove(cube)
                new_cubes.append(cube)
                new_node = Node(new_cubes, new_arm, h(new_cubes, goalnode.cube_array), float('inf'), current, [])
                current.children.append(new_node)

    return None
