# class reader:
#     def __init__(self, filename):
#         self.graph_dict = []
#         self.adjMatrix = [[]]
#         self.filename = filename

#     def getF

import math


class Node:
    def __init__(self, name=None, x=None, y=None):
        self.name = name
        self.x = x
        self.y = y
        self.distance = 0

    def printNode(self):
        print(self.x)


class Graph(object):
    # Inisialisasi
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = []
        self.__graph_dict = graph_dict

    def getGraph(self):
        return self.__graph_dict

    # Menambahkan simpul ke graf
    def tambah_simpul(self, simpul):
        duplicate = False
        for node in self.__graph_dict:
            if (node.name == simpul.name):
                duplicate
        if (not duplicate):
            self.__graph_dict.append(simpul)

    # # Menambahkan sisi ke graf

    # def tambah_sisi(self, simpul1, simpul2):
    #     if simpul1 in self.__graph_dict:
    #         self.__graph_dict[simpul1].append(simpul2)
    #     else:
    #         self.__graph_dict[simpul1] = [simpul2]

    # Print Graph
    def print_graph(self):
        for i in range(len(self.__graph_dict)):
            print(f"nama simpul: {self.__graph_dict[i].name}")
            print(
                f"posisi : ({self.__graph_dict[i].x},{self.__graph_dict[i].y})")

    # Mendapatkan idx simpul
    def getSimpulIdx(self, simpul):
        for i in range(len(self.__graph_dict)):
            if (simpul.name == self.__graph_dict.name):
                return i

    # def euclideanDistance(self, simpul1, simpul2, adjMatrix):
    #     found = True
    #     if (adjMatrix[self.getSimpulIdx(simpul1)]
    #             [self.getSimpulIdx(simpul2)] == 0):
    #         return -1
    #     else:
    #         distance = math.sqrt(
    #             (simpul1.x - simpul2.x)**2 + (simpul1.y - simpul2.y)**2)
    #         return distance
    def getNeighbor(self, simpul, adjMatrix):
        neighbor = []
        simpulIdx = self.getSimpulIdx(simpul)
        for i in range(len(adjMatrix)):
            if (adjMatrix[simpulIdx][i] != 0):
                neighbor.append(self.__graph_dict[i])

    def euclideanDistance(self, simpul, goal):
        distance = math.sqrt(
            (simpul.x - goal.x)**2 + (simpul.y - goal.y)**2)
        return distance


def baca_file(nama_file):
    # Membaca sebuah nama_file dan menaruhnya ke dalam array input
    hasilRead = []
    f = open(nama_file, "r")
    for line in f:
        hasilRead.append(line.strip("\n"))
    f.close()
    # Inisialisasi variabel di awal
    N = int(hasilRead[0])
    G = Graph()
    M = []
    # Memasukkan simpul-simpul di graf
    for i in range(1, N + 1):
        temp = hasilRead[i].split(" ")
        G.tambah_simpul(Node(temp[0], temp[1], temp[2]))
    # Membuat adjacency matriks
    for i in range(N + 1, 2 * N + 1):
        temp = hasilRead[i].split(" ")
        for j in range(len(temp)):
            temp[j] = int(temp[j])
        M.append(temp)
    return G, M


G, M = baca_file("test.txt")
# neighbor = G.getNeighbor(G.__graph_dict[0], M)
# print(neighbor)


# def AStar(Graph, start, end):
#     for i in range(len(G.__graph_dict)):
#         temp = G.__graph_dict[i]
#         G.__graph_dict[i].distance = G.euclideanDistance(temp, end)
#     queue = []
#     queue.append(G.__graph_dict[0])
#     while (len(queue) != 0):
#         neighbor =
