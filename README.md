# ※ A* python Implementation and graph visualization
We've done a simple implementation of the A* algorithm on a given project. The goal was to provide a starting point encoded as an array of cubes and a robotic arm, and then achieve the wanted result in the minimal number of operations. 

## ※ Disclaimer
- This school project was done under a weekend, and may have trouble with larger tests samples. The project comes with a premade `main.py` file containing an already existing starting node and an existing final node. 
- For windows users, both the python graphviz and the graphviz library are mandatory. You can get these here https://pypi.org/project/graphviz/ and here https://graphviz.org/
- For UNIX users, running `sudo apt install graphviz
` should be enough
- For MacOS users, you can simply run `sudo port install graphviz`
- The algorithms used outside of A* may slow down performance, thus slowing down runtime on larger test runs
- Although both the heuristic and the real cost value of have already been implemented, you can still create your own and pass them as a parameter to the `astar()` function, which may give better results as the heuristic hasn't been tested thoroughly yet and may not be the most efficient one.

## ※ Running `main.py` and basic explanation of the classes
1. First, create an array of cubes with the corresponding constructor functions. Then create a starting node using this list ( You will need a heuristic value that you can either calculate yourself or create the goal node first and use the heuristic function. )
2. Create another array of cubes with the corresponding constructor functions and assign it to the goal node.
3. The A* algorithm was made so it returns the path from the goal node, although the `path_to_tree` function only needs the starting node.
4. Indicate the `*.png` you want the anytree library to use, and it should create an image of the tree generated by the A* algorithm.
