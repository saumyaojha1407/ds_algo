class Graph(object):
    def __init__(self, size):
        self.adjacent_matrix = []
        for i in range(size):
            self.adjacent_matrix.append([0 for j in range(size)])
        self.size = size

    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex : v1 = {}, v2 =  {}".format(v1, v2))
        self.adjacent_matrix[v1][v2] = 1
        self.adjacent_matrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex : v1 = {}, v2 =  {}".format(v1, v2))
        self.adjacent_matrix[v1][v2] = 0
        self.adjacent_matrix[v2][v1] = 0

    def print_adjacent_matrix(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.adjacent_matrix[i][j])
            print()


def main():
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)

    g.print_adjacent_matrix()


if __name__ == '__main__':
    main()