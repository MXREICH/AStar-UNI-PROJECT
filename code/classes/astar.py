
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
    # 1. mettre le nœud de départ dans OUVERT
    open_set = list()
    open_set.append(startnode)
    closed_set = list()

    # 2. SI OUVERT est vide, sortir avec Echec, SINON continuer
    while len(open_set) > 0:
        # 3. enlever le nœud de la tête de OUVERT et le mettre dans FERME. Appeler ce nœud n
        n = open_set.__getitem__(0)
        print(type(n))
        open_set.remove(open_set[0])
        closed_set.append(n)

        # 4. développer n en générant tous ses successeurs, ajouter à chacun de ses successeurs un pointeur vers n.
        for x in n.cube_array:
            if n.arm.free:
                y = x
                newnode = n
                if y.on is None:
                    if newnode.arm.hold(y):
                        newnode.parent = n
                        n.children.append(newnode)
                else:
                    if newnode.arm.hold2(y, y.on):
                        newnode.parent = n
                        n.children.append(newnode)
            else:
                newnode = n
                if x.held:
                    y = x
                    if newnode.arm.put(y):
                        newnode.parent = n
                        n.children.append(newnode)
                newnode2 = n
                if x.held:
                    z = x
                    for i in newnode2.cube_array:
                        if i != x:
                            newnode3 = newnode2
                            if newnode3.arm.put(z, i):
                                newnode3.parent = n
                                n.children.append(newnode)

        # 5. Si un quelconque successeur de n est un noeud but, sortir avec la solution obtenue en remontant à travers les pointeurs, sinon continuer
        for x in n.children:
            if h(x, goalnode) == 0:
                while x != startnode:
                    go_up_path = [x]
                    x = x.parent
                go_up_path.append(startnode)
                go_up_path.reverse()
                return go_up_path

        # 6. Pour tout successeur x de n
        for x in n.children:
            # a. calculer f(x)
            f = {x: x.heuristic_value + x.cost_value}
            # b. si x n'est ni dans OUVERT ni dans FERME l'ajouter à OUVERT
            if x not in open_set and x not in closed_set:
                open_set.add(x)

            # c.i si x figure dans OUVERT ou FERME, comparer la nouvelle valeur de g(x) à l'ancienne. Si l'ancienne
            # est inferieure ou égale alors elminer le noeud, sinon subst. valeur à l'ancienne
            if x in open_set or x in closed_set:
                if x.cost_value > n.cost_value + 1:
                    g(x)
                    x.parent = n
                    # c.ii si le noeud x est dans FERME, remettre dans OUVERT
                    if x in closed_set:
                        closed_set.remove(x)
                        open_set.add(x)

            # d. ordonner OUVERT selon f(x)
            open_set = sorted(f.items())
        # 7. aller à 2.

    return None
