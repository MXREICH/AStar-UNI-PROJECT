def astar(h,g,startnode, goalnode):
    """
    1. mettre le nœud de départ dans OUVERT
    2. SI OUVERT est vide, sortir avec Echec, SINON continuer
    3. enlever le nœud de la tête de OUVERT et le mettre dans FERME. Appeler ce nœud n
    4. développer n en générant tous ses successeurs, ajouter à chacun de ses successeurs un pointeur vers n.
    5. SI l’un quelconque de ses successeurs est un nœud but, sortir avec la solution obtenue en remontant à travers les pointeurs, SINON continuer.
    6. pour tout successeur n’ de n :
    a. calculer f(n’)
    b. si n’ n’est ni dans OUVERT ni dans FERME l’ajouter à OUVERT
    c. SI n’ figure dans OUVERT ou FERME, comparer la nouvelle valeur de g(n’) à l’ancienne. SI l’ancienne est inférieure ou égale, alors éliminer le
    nœud nouvellement généré, sinon, substituer la nouvelle valeur à l’ancienne (s’assurer que le pointeur reste dirigé vers n). SI le nœud
    correspond figure dans FERME, la remettre dans OUVERT.
    d. ordonner OUVERT suivant la fonction f(n)
    7. aller à 2
    """