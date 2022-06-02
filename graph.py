class Graph:
    def __init__(self, name):
        self.name = name
        self.list = {}
        self.e_list = {}
        self.v_list = []


        self.e_oriented_list = []
        self.e_not_oriented_list = []


        self.v_names = {}
        self.v_colors = {}
        self.e_amount = 0
        self.v_amount = 0


    def print(self):
        for v1 in self.list:
            if len(self.list[v1]) != 0:
                for v2 in self.list[v1]:
                    if (v1, v2) in self.e_oriented_list:
                        print(v1,'->',v2)
                    elif (v1, v2) in self.e_not_oriented_list or (v2,v1) in self.e_not_oriented_list:
                        print(v1,'=',v2)
            else:
                print(v1)


    def return_v_amount(self):
        return self.v_amount
    def return_e_amount(self):
        return self.e_amount


    # add EDGE between vertex1 to vertex2
    def add_not_oriented_e(self, vertex1, vertex2):
        # v1 -> v2 and v1 <- v2
        self.add_v(vertex1)
        self.add_v(vertex2)
        #if vertex1 in self.list.keys():
        self.list[vertex1].append(vertex2)
        self.e_amount += 1

        #if vertex2 in self.list.keys():
        self.list[vertex2].append(vertex1)

        self.e_list['e'+str(self.e_amount)] = (vertex1, vertex2)

        self.e_not_oriented_list.append((vertex1, vertex2))


    # add EDGE from vertex1 to vertex2
    def add_oriented_e(self, vertex1, vertex2):
        # v1 -> v2
        self.e_amount += 1
        self.add_v(vertex1)
        self.add_v(vertex2)
        self.list[vertex1].append(vertex2)

        self.e_list['e'+str(self.e_amount)] = (vertex1, vertex2)

        self.e_oriented_list.append((vertex1, vertex2))

    # add VERTEX
    def add_v(self, vertex):

        #vertex = 'v' + str(self.v_amount)
        #v = Vertex(self, vertex)
        #self.v_list.append(v)
        if vertex not in self.list:
            self.v_amount += 1
            self.list[vertex] = []

    # set VERTEX NAME
    def set_v_name(self, vertex, name):
        if vertex in self.v_list:
            vertex.name = name
            self.v_names[vertex] = name
    # set VERTEX COLOR
    def set_v_color(self, vertex, color):
        if vertex in self.list.keys():
            self.v_colors[vertex] = color


    def del_v(self, vertex):
        if vertex in self.list:
            for v in self.list:
                if vertex is not v and vertex in self.list[v]:
                    print(vertex,'->', v)
                    self.e_amount -= 1
                    self.list[v].remove(vertex)

        for v in self.list[vertex]:
            self.e_amount -= 1

        self.list.pop(vertex)
        self.v_amount -= 1

    def del_e(self, vertex1, vertex2):
        # if oriented
        if (vertex1, vertex2) in self.e_oriented_list:
            if vertex2 in self.list[vertex1]:
                self.list[vertex1].remove(vertex2)
                self.e_amount -= 1
        # if not oriented
        elif (vertex1, vertex2) in self.e_not_oriented_list:
            self.e_amount -= 1
            if vertex2 in self.list[vertex1]:
                self.list[vertex1].remove(vertex2)
            if vertex1 in self.list[vertex2]:
                self.list[vertex2].remove(vertex1)




    def gamilton(self):
        pass









class Vertex:
    def __init__(self, graph, sign):
        self.graph = graph
        self.sign = sign
        self.list = []
        self.name = ''

    def set_name(self, name):
        self.name = name

    def add_e(self, vertex):
        self.list.append(vertex)

    def remove_e(self, vertex):
        if vertex in self.list:
            self.list.remove(vertex)

class Edge:
    def __init__(self, graph, type, vertex1, vertex2):
        self.graph = graph
        self.type = type
        self.v1 = vertex1
        self.v2 = vertex2

    def delete(self):
        pass