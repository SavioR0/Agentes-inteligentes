from asyncio import QueueEmpty
import queue
from anytree import Node, RenderTree

# Criação da árvore de estados


def createTree():
    # root
    root = Node("m0c0m3c3")

    # Level 1
    m0c2m3c1 = Node("m0c2m3c1", parent=root)
    m1c1m2c2 = Node("m1c1m2c2", parent=root)

    # Level 2
    m0c1m3c2 = Node("m0c1m3c2", parent=m0c2m3c1)

    # Level 3
    m0c3m3c0 = Node("m0c3m3c0", parent=m0c1m3c2)

    # Level 4
    m0c2m3c1 = Node("m0c2m3c1", parent=m0c3m3c0)

    # Level 5
    m2c2m1c1 = Node("m2c2m1c1", parent=m0c2m3c1)

    # Level 6
    m1c1m2c2 = Node("m1c1m2c2", parent=m2c2m1c1)

    # Level 7
    m3c1m0c2 = Node("m3c1m0c2", parent=m1c1m2c2)

    # Level 8
    m3c0m0c3 = Node("m3c0m0c3", parent=m3c1m0c2)

    # Level 9
    m3c2m0c1 = Node("m3c2m0c1", parent=m3c0m0c3)

    # Level 10
    m3c1m0c2 = Node("m3c1m0c2", parent=m3c2m0c1)

    # Level 10
    m3c3m0c0 = Node("m3c3m0c0", parent=m3c1m0c2)

    return root


# Solução encontrada
def solution(node):
    print("\n\n ---------------------------------------------")
    print("\t NÓ SOLUÇÃO ENCONTRADO !", node.name)
    print(" ---------------------------------------------")


# Solução não encontrada
def failure():
    print(" FALHA AO ENCONTRAR NÓ OBJETIVO! :(")


# Return Queue
def returnQueue(node):
    frontier = []
    for nodeFrontier in node.children:
        frontier.append(nodeFrontier)
    return frontier


# Print nós explorados
def exploredNodes(explored):
    count = 0
    print("\n\n--------------------- NÓS EXPLORADOS ------------------------")
    for nodes in explored:
        print(nodes.name, end=", ")
        count = count + 1
        if count % 6 == 0:
            print()
    print("\n--------------------------------------------------------------")


# Busca em largura
def breadthFirstSearch(root, goal):

    node = root
    if node.name == goal:
        return solution(node)
    frontier = returnQueue(node)
    explored = []
    print("Tamanho fronteira : ", len(frontier))
    while len(frontier) != 0:
        node = frontier.pop(0)
        explored.append(node)

        children = returnQueue(node)
        while len(children) != 0:
            print("Tamanho da fila de filhos:", len(children))
            child = children.pop(0)

            print("Child :", child.name)
            if (child not in explored) and (goal == child.name):
                exploredNodes(explored)
                return solution(child)
            frontier.append(child)
    exploredNodes(explored)
    return failure


# Print Arvore
def printTree(root):
    print("\n\n------------------ARVORE DE ESTADOS----------------------")
    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))
    print("\n---------------------------------------------------------")
