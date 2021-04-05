import math


class Node:
    def __init__(self, name, x, y, euclidean=None):
        self.name = name
        self.x = x
        self.y = y
        self.euclidean = 0
        self.weight = 0
        self.parent = None

    def getName(self):
        return self.name

    def setEuclidean(self, distance):
        self.euclidean = distance

    def setWeight(self, weight):
        self.weight = weight


class Graph:
    def __init__(self):
        self.nodeArray = []

    def addNode(self, node):
        self.nodeArray.append(node)

    def euclideanDistance(self, node, goal):
        distance = math.sqrt(
            (node.x - goal.x)**2 + (node.y - goal.y)**2)
        return distance

    def getNodeIdx(self, node):
        for i in range(len(self.nodeArray)):
            if (node.name == self.nodeArray[i].getName()):
                return i

    def getNeighbor(self, node, adjMatrix):
        neighbor = []
        nodeIdx = self.getNodeIdx(node)
        for i in range(len(adjMatrix)):
            if (adjMatrix[nodeIdx][i] != 0):
                neighbor.append(self.nodeArray[i])
        return neighbor


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
        G.addNode((Node(temp[0], float(temp[1]), float(temp[2]))))
    # Membuat adjacency matriks
    for i in range(N + 1, 2 * N + 1):
        temp = hasilRead[i].split(" ")
        for j in range(len(temp)):
            temp[j] = int(temp[j])
        M.append(temp)
    return G, M


def AStar(G, M, start, end):
    # Menginisialisasi euclidean distance dari masing-masing node ke
    # end node
    for i in range(len(G.nodeArray)):
        distance = G.euclideanDistance(G.nodeArray[i], end)
        G.nodeArray[i].setEuclidean(distance)
    # Inisialisasi variabel lain
    queue = []  # Queue untuk menampung semua path yang ada
    # Queue diisi dengan list dari start node terlebih dahulu
    queue.append([start])
    found = False  # Sudah menemukan hasil
    while(not found and queue != []):
        # Sort queue berdasarkan nilai euclidean dan jarak dari jalur
        # awal ke node sementara
        queue = sorted(queue, key=lambda x: x[len(
            x) - 1].euclidean + x[len(x) - 1].weight)
        # Pop elemen pertama atau elemen dengan nilai jalur yang
        # paling rendah
        temp = queue.pop(0)
        # Mendapat semua neighbor dari node paling akhir dari temp
        neighbor = G.getNeighbor(temp[len(temp) - 1], M)
        for i in range(len(neighbor)):
            subResult = temp.copy()
            # Mengakhiri penelusuran jika sudah ditemukkan node endnya
            if(neighbor[i].name == end.name):
                temp.append(neighbor[i])
                found = True
            # Mengubah nilai weight atau jarak dari node awal ke node
            # sementara
            neighbor[i].setWeight(G.euclideanDistance(
                neighbor[i], temp[len(temp) - 1]) + temp[len(temp) - 1].weight)
            # Kalau node belum pernah dikunjungi di jalur maka node
            # ditambahkan
            if (neighbor[i] not in subResult):
                subResult.append(neighbor[i])
                queue.append(subResult)
    # Mengembalikan jalur hasil yang disimpan di temp
    if found:
        return (temp)
    else:
        return []
