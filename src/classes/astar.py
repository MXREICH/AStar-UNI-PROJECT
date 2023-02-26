from src.classes.heap import HNode


def heuristic1(currentnode, goalnode):
    n = len(goalnode.cube_array)
    it = 0
    for x, y in zip(goalnode.cube_array, currentnode.cube_array):
        if hash(x) == hash(y):
            it = it + 1
    return n - it


def realcost1(currentnode):
    currentnode.cost_value = currentnode.cost_value + 1


def f(node):
    return node.heuristic_value + node.cost_value


def prnt(arr):
    for x in arr:
        print(x)


def eqnode(node1, node2):
    for x, y in zip(node1.cube_array, node2.cube_array):
        if x.free != y.free:
            return False
        if x.held != y.held:
            return False
        if x.ontable != y.ontable:
            return False
        if x.on is None and y.on is not None:
            return False
        if x.on is not None and y.on is None:
            return False
        if not(x.on is None and y.on is None) and x.on.name != y.on.name:
            return False
    return True


def findarr(node_arr, node):
    for nodei in node_arr:
        if eqnode(nodei, node):
            return nodei
    return None


def astar(h, g, startnode, goalnode):
    # 1. mettre le nœud de départ dans OUVERT
    open_list = [startnode]
    closed_list = []
    # 2. SI OUVERT est vide, sortir avec Echec, SINON continuer
    while len(open_list) > 0:
        # print(len(open_list), "close:", len(closed_list))

        # 3. enlever le nœud de la tête de OUVERT et le mettre dans FERME. Appeler ce nœud n
        n: HNode = open_list[0]
        open_list.remove(n)
        closed_list.append(n)
        # 4. développer n en générant tous ses successeurs, ajouter à chacun de ses successeurs un pointeur vers n.
        for x in n.cube_array:
            newnode = n.birth()
            if n.arm.free and x.free:
                newnode.arm_hold(x, x.on)
                newnode.heuristic_value = h(newnode, goalnode)
                g(newnode)
                n.children.append(newnode)
            elif n.arm.free and not x.free:
                continue
            elif not n.arm.free and x.free:
                continue
            else:
                if x.held:
                    newnode.arm_put(x.cpy())
                    newnode.heuristic_value = h(newnode, goalnode)
                    g(newnode)
                    n.children.append(newnode)
                    for i in n.cube_array:
                        if not i.free or i == x:
                            continue
                        newnode2 = n.birth()
                        newnode2.arm_put(x.cpy(), i.cpy())
                        newnode2.heuristic_value = h(newnode2, goalnode)
                        g(newnode2)
                        n.children.append(newnode2)
        # 5. Si un quelconque successeur de n est un noeud but, sortir avec la solution obtenue en remontant à
        # travers les pointeurs, sinon continuer
        for x in n.children:
            if x.heuristic_value == 0:
                go_up_path = []
                reference = x
                while reference.parent is not None:
                    go_up_path.append(reference)
                    reference = reference.parent
                go_up_path.append(startnode)
                go_up_path.reverse()
                return go_up_path

        # 6. Pour tout successeur x de n
        for x in n.children:
            # b. si x n'est ni dans OUVERT ni dans FERME l'ajouter à OUVERT
            x_open = findarr(open_list, x)
            x_close = findarr(closed_list, x)
            if x_open is None and x_close is None:
                open_list.append(x)
            # c.i si x figure dans OUVERT ou FERME, comparer la nouvelle valeur de g(x) à l'ancienne. Si l'ancienne
            # est inferieure ou égale alors elminer le noeud, sinon substituer la nouvelle valeur à l'ancienne
            elif x_open is not None:
                if x.cost_value < x_open.cost_value:
                    open_list.remove(x_open)
                    open_list.append(x)
            else:
                if x.cost_value < x_close.cost_value:
                    closed_list.remove(x_close)
                    open_list.append(x)

            # d. ordonner OUVERT selon f(x)
            # a. on appelle également la fonction f qui retourne pour un état donné sa valeur g+h
        open_list = sorted(open_list, key=f)

        # 7. aller à 2.

    raise Exception("OPEN_LIST < 0 SANS SOLUTION")
