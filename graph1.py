from random import randint


class Vertex:
    def __init__(self, graph, sign, index):
        self.graph = graph
        self.sign = sign
        self.index = index
        self.degree = []
        self.degrees = 0
        self.edges = []
        self.color = ''
        self.text = ''


        self.visited = []
        self.not_visited = self.degree
        self.connection_count = 1
        self.connection = {}
        self.prev = 0

        self.connection_path = []

        self.min_path = {}
        self.max_path = {}
        self.extr = 0


        self.path_values = []

        self.gam_path = []

class Edge:
    def __init__(self, graph, vertex1, vertex2, type, sign):
        self.graph = graph
        self.sign = sign
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.type = type
        self.color = ''



class Graph:
    def __init__(self):
        self.name = ''
        self.type = 0
        self.v_list = []
        self.e_list = []
        self.matrix = []
        self.name = ''

        self.v_amount = 0
        self.e_amount = 0
        # gam cycles
        self.gam_cycles = []

        self.min_path_matrix = []
        # far vertex
        self.far_vertex = 0
        #center
        self.center_vertex = 0
        # graph_radius
        self.graph_radius = 0
        # diameter
        self.diameter = 0









    # set graph NAME
    def set_name(self, name):
        self.name = name

    def print_matrix(self):
        for list in self.matrix:
            print(list)
        for v in self.v_list:
            print(v.sign, v.index)

    def return_v_amount(self):
        return len(self.v_list)
    def return_e_amount(self):
        return len(self.e_list)

    def return_degrees(self):
        for v in self.v_list:
            print(v.sign,': ',v.degrees)
    def return_v_degree(self, vertex):
        for v in self.v_list:
            if v.sign == vertex:
                print(v.sign,': ',v.degrees)




    # -------------- CONNECTION -----------------
    # return True if it is
    # False if it is not
    def is_connected(self):
        count = 0
        for v in self.v_list:
            path = []
            kol, path = self.dfs_connected(v, v, path)
            v.connection_path = path
            if kol == len(self.v_list):
                count += 1
                return True
            # if count == len(self.v_list) or count == len(self.v_list) - 1:
            #     return True

        return False


        # # Если для ориентироавнного
        # count = 0
        # for v in self.v_list:
        #     path = []
        #     kol, path = self.dfs_connected(v, v, path)
        #     v.connection_path = path
        #     print(v.sign, 'kolvo',kol, 'path-', path)
        #     if kol == len(self.v_list):
        #         count += 1
        # if count == len(self.v_list) or count == len(self.v_list) - 1:
        #     return True
        # else:
        #     return False

    def dfs_connected(self, v0, vertex, path):
        all_vis = 1
        path.append(vertex.sign)
        for v in vertex.degree:
            if v.sign not in path:
                all_vis1, path = self.dfs_connected(v0, v, path)
                all_vis += all_vis1

        return all_vis, path

    # make graph the connected one
    def make_connected(self):

        for vertex in self.v_list:
            # check if our graph is really not connected
            if len(vertex.connection_path) != len(self.v_list):
                # make a list of all vertexes signs
                vertexes_sign_list = []
                for v in self.v_list:
                    vertexes_sign_list.append(v.sign)

                # create a list of not vertexes that we can connect with our not connected one
                # to make graph connected
                candidates_to_connect_with = list(filter(lambda s: s in vertex.connection_path, vertexes_sign_list))
                # a list of not connected vertexes
                not_connected_vertexes = list(filter(lambda s: s not in vertex.connection_path, vertexes_sign_list))

                if len(not_connected_vertexes) != 0:
                    for v in self.v_list:
                        for v1 in not_connected_vertexes:
                            if v.sign == v1:
                                self.add_e_oriented(vertex.sign, v.sign, '', 1)
                                if self.is_connected():
                                    return True
            return False

    # -------------------------------------------





    # -------------- GAMILTON -----------------
    # find GAMILTON CYCLES
    def dfs_gamilton(self, v0, edges, path, not_visited_vertexes):
        flag = False

        for e in edges:
            vertex = e.vertex2
            if vertex in not_visited_vertexes:
                if vertex == v0:
                    # print('here',vertex.sign, len(self.v_list)-1, len(path), len(not_visited_vertexes))
                    if len(path) == len(self.v_list)-1 and len(not_visited_vertexes) == 1:
                        path.append(vertex.sign)
                        new_path = []
                        new_path.append(v0.sign)
                        for v in path:
                            new_path.append(v)
                        self.gam_cycles.append(new_path)
                        return True

                else:
                    path.append(vertex.sign)
                    not_visited_vertexes.remove(vertex)
                    flag = self.dfs_gamilton(v0, vertex.edges,  path, not_visited_vertexes)
                    if flag == False:
                        path.remove(vertex.sign)
                        not_visited_vertexes.append(vertex)
                    else:
                        return flag
        return flag


    def is_gamilton(self):
        self.gam_cycles = []

        for v in self.v_list:
            not_visited_vertexes = []

            print('-------vertex', v.sign)
            for vertex in self.v_list:
                if vertex != v:
                    not_visited_vertexes.append(vertex)
                #print(e.type,':',e.vertex1.sign, '->', e.vertex2.sign)
            not_visited_vertexes.append(v)
            path = []
           # path.append(v.sign)

            f = self.dfs_gamilton(v, v.edges, path, not_visited_vertexes)
        if len(self.gam_cycles) != 0:
            print(self.gam_cycles)
            return True
        else:
            return False
    # -----------------------------------------


    # центр - множество вершин
    def center(self):
        min = 0
        min_v = 0
        for v in self.v_list:
            if len(v.degree) <= min:
                min = len(v.degree)
                min_v = v.sign
        return min_v


    # add VERTEX
    def add_v(self, vertex):
        self.v_amount += 1
        v = Vertex(self, vertex, self.v_amount-1)
        self.v_list.append(v)

        if len(self.matrix) == 0:
            self.matrix.append([0])
        else:
            count = 0
            for list in self.matrix:
                list.append(0)
                count += 1
            # add new vertex to the matrix
            new_list = []
            for i in range(0, count+1):
                new_list.append(0)
            self.matrix.append(new_list)

    def remove_v(self, vertex):
        for v in self.v_list:
            if v.sign == vertex:
                del_v = v
                # remove all EDGES
                for e in self.e_list:
                    if e.vertex1 == v:
                        self.remove_e(e.sign)
                    elif e.vertex2 == v:
                        self.remove_e(e.sign)
                # if len(v.degree) != 0:
                #     for other_v in v.degree:
                #         if v in other_v.degree:
                #             other_v.degree.remove(v)
                #             e = self.search_e(v, other_v)
                #             if e != None:
                #                 other_v.edges.remove(e)
                #             e = self.search_e(other_v, v)
                #             if e != None:
                #                 other_v.edges.remove(e)
                #             self.remove_e(e.sign)

        for count, list in enumerate(self.matrix):
            list.pop(del_v.index)

        # low the vertexes indexes
        for i in range(del_v.index, len(self.v_list)):
            self.v_list[i].index -= 1

        self.matrix.pop(del_v.index)
        self.v_list.remove(del_v)
        self.v_amount -= 1

    def set_v_color(self, vertex, color):
        for v in self.v_list:
            if v.sign == vertex:
                v.color = color


    def find_vertex(self, vertex):
        for v in self.v_list:
            if v.sign == vertex:
                return v



    def add_e_oriented(self, vertex1, vertex2, name, type):
        #NOT SURE if we shoul add new vertexes
        #v1, v2 = None, None

        v1 = self.find_vertex(vertex1)
        v2 = self.find_vertex(vertex2)


        if v1 == None or v2 == None:
            return False
        else:
            self.e_amount += 1
            if name == '':
                sign = 'e' + str(self.e_amount)
            else:
                sign = name

            if type == 11:
                e = Edge(self, v1, v2, 1, sign)
                self.e_list.append(e)
                v1.degree.append(v2)
                v1.edges.append(e)
                v1.degrees += 1
                v2.degrees += 1

                for count, list in enumerate(self.matrix):
                    if v1.index == count:
                        for i in range(0, len(list)):
                            if i == v2.index:
                                list[i] += 1
                                break
                return True




            elif type == 1:
                e = Edge(self, v1, v2, 1, sign)
                self.e_list.append(e)
                v1.degree.append(v2)
                v1.edges.append(e)
                v1.degrees += 1
                v2.degrees += 1
            elif type == 2:
                e = Edge(self, v1, v2, 2, sign)
                self.e_list.append(e)
                v1.degree.append(v2)
                v1.edges.append(e)
                v1.degrees += 1
                v2.degrees += 1


            # add EDGE to the matrix
            for count, list in enumerate(self.matrix):
                if v1.index == count:
                    for i in range(0, len(list)):
                        if i == v2.index:
                            list[i] += 1
                            break
            return True


    def add_e_not_oriented(self, vertex1, vertex2, name):
        v1, v2 = None, None
        for v in self.v_list:
            if v.sign == vertex1:
                # self.add_e_oriented(vertex1, vertex2, name, 2)
                # v.degrees -= 1
                v1 = v
            elif v.sign == vertex2:
                # self.add_e_oriented(vertex2, vertex1, name, 2)
                # v.degrees -= 1
                v2 = v
        if v1 == None or v2  == None:
            return False
        else:
            self.e_amount += 1
            if name == '' or name == ' ':
                sign = 'e' + str(self.e_amount)
            else:
                sign = name
            e = Edge(self, v1, v2, 2, sign)

            # print(e.vertex1.sign,'->',e.vertex2.sign)
            self.e_list.append(e)


            v1.degree.append(v2)
            v2.degree.append(v1)
            v1.edges.append(e)
            v2.edges.append(e)
            v1.degrees += 1
            v2.degrees += 1
            #
            # # add EDGE to the matrix
            for count, list in enumerate(self.matrix):
                if v1.index == count:
                    for i in range(0, len(list)):
                        if i == v2.index:
                            list[i] += 1

                elif v2.index == count:
                    for i in range(0, len(list)):
                        if i == v1.index:
                            list[i] += 1
            return True


    # remove EDGE
    def remove_e(self, edge):
        count = 0
        for e in self.e_list:
            if e.sign == edge:
                count += 1
                # print('edge', e.sign)
                v1 = e.vertex1
                v2 = e.vertex2
                # print(v1.sign)
                # for e in v1.edges:
                #     print(e.sign)
                # print(v2.sign)
                # for e in v2.edges:
                #     print(e.sign)
                if e.type == 2:
                    for count, list in enumerate(self.matrix):
                        if v1.index == count:
                            for i in range(0, len(list)):
                                if i == v2.index:
                                    if e in v1.edges:
                                        list[i] -= 1
                                        v1.edges.remove(e)
                                        v1.degree.remove(v2)
                                        v1.degrees -= 1


                        elif v2.index == count:
                            for i in range(0, len(list)):
                                if i == v1.index:
                                    if e in v2.edges:
                                        list[i] -= 1
                                        v2.edges.remove(e)
                                        v2.degree.remove(v1)
                                        v2.degrees -= 1

                    #self.e_list.remove(e)


                elif e.type == 1:
                    for count, list in enumerate(self.matrix):
                        if v1.index == count:
                            for i in range(0, len(list)):
                                if i == v2.index:
                                    list[i] -= 1
                                    v1.edges.remove(e)
                                    #v2.edges.remove(e)
                                    v1.degree.remove(v2)
                                    v1.degrees -= 1
                                    v2.degrees -= 1
                                    #v2.degree.remove(v1)
                self.e_list.remove(e)


        if count != 0:
            self.e_amount -= 1
            return True
        else:
            return False




    def set_e_color(self, edge, color):
        for e in self.e_list:
            if e.sign == edge:
                e.color = color

    def search_e(self, v1, v2):
        for e in self.e_list:
            if (e.vertex1 == v1 and e.vertex2 == v2) or (e.vertex1 == v2 and e.vertex2 == v1):
                return e
        return None

    def search_multiple_e(self):
        # NOT SURE if we shoul add new vertexes
        # v1, v2 = None, None
        multi_edges = []
        for e in self.e_list:
            v1 = e.vertex1
            v2 = e.vertex2
            print('for ', v1.sign, v2.sign, end='')

            for e2 in self.e_list:
                    if (e2.vertex1 == v1 and e2.vertex2 == v2) or (e2.vertex1 == v2 and e2.vertex2 == v1):
                        if e2 != e:
                            if e2 not in multi_edges:
                                print('found ', e2.vertex1.sign, e2.vertex2.sign)
                                multi_edges.append(e2)
        if len(multi_edges) >= 2:
            return multi_edges
        else:
            return []


    def dfs_min_path(self, v0, prev_vertex, edges, not_visited_edges, count, path):
        flag = False
        if self.is_gamilton():
            if count + 1 == len(self.v_list):
                return True, count


        for e in edges:
            if e.type == 1:
                vertex = e.vertex2
                #if e in not_visited_edges:

                count += 1
                not_visited_edges.remove(e)

                if path[vertex.sign] > count:
                    path[vertex.sign] = count
                elif path[vertex.sign] == 0:
                    path[vertex.sign] = count

                print('from', e.vertex1.sign, ' to', e.vertex2.sign, path)
                if len(not_visited_edges) == 0:
                    flag = True
                    return flag, count
                buf_edges = []
                for buf in not_visited_edges:
                    buf_edges.append(buf)
                for e in vertex.edges:
                    not_visited_edges.append(e)
                #visited += 1
                flag, k = self.dfs_min_path(v0, vertex, vertex.edges, not_visited_edges, count, path)
                if flag == False:
                    not_visited_edges = []
                    count -= 1
                    #visited -= 1
                    for b in buf_edges:
                        not_visited_edges.append(b)

                    #count -= 1
                else:
                    return flag, count
            elif e.type == 2:
                if e.vertex1 == prev_vertex:
                    vertex = e.vertex2
                    if e in not_visited_edges:

                        count += 1
                        not_visited_edges.remove(e)

                        if path[vertex.sign] > count:
                            path[vertex.sign] = count
                        elif path[vertex.sign] == 0:
                            path[vertex.sign] = count

                        # print('from', e.vertex1.sign, ' to', e.vertex2.sign, path)
                        if len(not_visited_edges) == 0:
                            flag = True
                            return flag, count
                        buf_edges = []
                        for buf in not_visited_edges:
                            buf_edges.append(buf)
                        for e in vertex.edges:
                            not_visited_edges.append(e)

                        flag, k = self.dfs_min_path(v0, vertex, vertex.edges, not_visited_edges, count, path)
                        if flag == False:
                            not_visited_edges = []
                            count -= 1
                            for b in buf_edges:
                                not_visited_edges.append(b)

                            # count -= 1
                        else:
                            return flag, count
                elif e.vertex2 == prev_vertex:
                    vertex = e.vertex1
                    if e in not_visited_edges:

                        count += 1
                        not_visited_edges.remove(e)

                        if path[vertex.sign] > count:
                            path[vertex.sign] = count
                        elif path[vertex.sign] == 0:
                            path[vertex.sign] = count

                        # print('from', e.vertex1.sign, ' to', e.vertex2.sign, path)
                        if len(not_visited_edges) == 0:
                            flag = True
                            return flag, count
                        buf_edges = []
                        for buf in not_visited_edges:
                            buf_edges.append(buf)
                        for e in vertex.edges:
                            not_visited_edges.append(e)

                        flag, k = self.dfs_min_path(v0, vertex, vertex.edges, not_visited_edges, count, path)
                        if flag == False:
                            not_visited_edges = []
                            count -= 1
                            for b in buf_edges:
                                not_visited_edges.append(b)

                            # count -= 1
                        else:
                            return flag, count

        return flag, count

    def dfs_max_path(self, v0, prev_vertex, edges, not_visited_edges, count, path):
        flag = False
        if self.is_gamilton():
            if count + 1 == len(self.v_list):
                return True, count

        for e in edges:
            if e.type == 1:
                vertex = e.vertex2
                if e in not_visited_edges:

                    count += 1
                    not_visited_edges.remove(e)
                    #visited += 1
                    if path[vertex.sign] < count:
                        path[vertex.sign] = count
                    elif path[vertex.sign] == 0:
                        path[vertex.sign] = count

                    # print('from', e.vertex1.sign, ' to', e.vertex2.sign, path)
                    if len(not_visited_edges) == 0:
                        flag = True
                        return flag, count
                    buf_edges = []
                    for buf in not_visited_edges:
                        buf_edges.append(buf)
                    for e in vertex.edges:
                        not_visited_edges.append(e)

                    flag, k = self.dfs_max_path(v0, vertex, vertex.edges, not_visited_edges, count, path)
                    if flag == False:
                        not_visited_edges = []
                        count -= 1
                        #visited -= 1
                        for b in buf_edges:
                            not_visited_edges.append(b)

                        # count -= 1
                    else:
                        return flag, count
            elif e.type == 2:
                if e.vertex1 == prev_vertex:
                    vertex = e.vertex2
                    if e in not_visited_edges:

                        count += 1
                        not_visited_edges.remove(e)

                        if path[vertex.sign] > count:
                            path[vertex.sign] = count
                        elif path[vertex.sign] == 0:
                            path[vertex.sign] = count

                        # print('from', e.vertex1.sign, ' to', e.vertex2.sign, path)
                        if len(not_visited_edges) == 0:
                            flag = True
                            return flag, count
                        buf_edges = []
                        for buf in not_visited_edges:
                            buf_edges.append(buf)
                        for e in vertex.edges:
                            not_visited_edges.append(e)

                        flag, k = self.dfs_max_path(v0, vertex, vertex.edges, not_visited_edges, count, path)
                        if flag == False:
                            not_visited_edges = []
                            count -= 1
                            for b in buf_edges:
                                not_visited_edges.append(b)

                            # count -= 1
                        else:
                            return flag, count
                elif e.vertex2 == prev_vertex:
                    vertex = e.vertex1
                    if e in not_visited_edges:

                        count += 1
                        not_visited_edges.remove(e)

                        if path[vertex.sign] > count:
                            path[vertex.sign] = count
                        elif path[vertex.sign] == 0:
                            path[vertex.sign] = count

                        # print('from', e.vertex1.sign, ' to', e.vertex2.sign, path)
                        if len(not_visited_edges) == 0:
                            flag = True
                            return flag, count
                        buf_edges = []
                        for buf in not_visited_edges:
                            buf_edges.append(buf)
                        for e in vertex.edges:
                            not_visited_edges.append(e)

                        flag, k = self.dfs_max_path(v0, vertex, vertex.edges, not_visited_edges, count, path)
                        if flag == False:
                            not_visited_edges = []
                            count -= 1
                            for b in buf_edges:
                                not_visited_edges.append(b)

                            # count -= 1
                        else:
                            return flag, count

        return flag, count

    def min_path(self):
        for vertex in self.v_list:
            path = {}
            not_visited_edges = []
            for e in self.e_list:
                not_visited_edges.append(e)

            for v in self.v_list:
                path[v.sign] = 0

            count = 0
            print('-----------------',vertex.sign)
            f, count = self.dfs_min_path(vertex, vertex, vertex.edges, not_visited_edges, count, path)
            vertex.min_path = path

        for v in self.v_list:
            print(v.sign, v.min_path)

        self.find_extr()


    # FAR VERTEX and graph_radius
    def find_extr(self):
        max_list = []
        for i in range(len(self.v_list)):
            max_list.append(0)

        for vertex in self.v_list:
            for i, value in enumerate(vertex.min_path):
                max_list[i] += vertex.min_path[value]

        far_vertex_search = 0
        far_vertex_index = 0
        for i, value in enumerate(max_list):
            if value > far_vertex_search:
                far_vertex_search = value
                far_vertex_index = i # far vertex index


        print('max', max_list, 'far_vertex index', far_vertex_index)

        # find FAR VERTEX
        for v in self.v_list:
            if v.index == far_vertex_index:
                self.far_vertex = v
                print('far vertex', self.far_vertex.sign)

                # set the len to the far vertex for each vertex
                for v in self.v_list:
                    for far in v.min_path:
                        if far == self.far_vertex.sign:
                            print('far', far)
                            v.extr = v.min_path[self.far_vertex.sign]

        # find graph_radius
        graph_radius = 20
        for i in max_list:
            if i != 0:
                if i < graph_radius:
                    graph_radius = i  # far vertex index
        if self.is_gamilton():
            self.graph_radius = graph_radius - 1
        else:
            self.graph_radius = graph_radius

        # self.graph_radius = graph_radius
        print('graph_radius', self.graph_radius)

        for v in self.v_list:
            if v.extr == self.graph_radius:
                self.center_vertex = v.sign


        for v in self.v_list:
            print(v.extr)



    def max_path(self):
        for vertex in self.v_list:
            path = {}
            not_visited_edges = []
            for e in self.e_list:
                not_visited_edges.append(e)

            for v in self.v_list:
                path[v.sign] = 0

            count = 0

            f, count = self.dfs_max_path(vertex, vertex, vertex.edges, not_visited_edges, count, path)
            vertex.max_path = path
        print('max path')
        for v in self.v_list:
            print(v.sign, v.max_path)

        self.find_diameter()

    def find_diameter(self):
        max_list = []
        for i in range(len(self.v_list)):
            max_list.append(0)

        for vertex in self.v_list:
            for i, value in enumerate(vertex.max_path):
                if max_list[i] < vertex.max_path[value]:
                    max_list[i] = vertex.max_path[value]

        print('max_list',max_list)
        diameter = 0
        for i in max_list:
            if i > diameter:
                diameter = i  # diameter
        self.diameter = diameter
        print('diameter', diameter)


# ---------------------- MULTIPLICATION -------------------------

    def dekart_multiplication(self, graph, dekart_graph):

        for v1 in self.v_list:
            for v2 in graph.v_list:
                new_v = v1.sign + v2.sign
                dekart_graph.add_v(new_v)
        for i in dekart_graph.v_list:
            print(i.sign)

        print(dekart_graph.v_amount)


        for list in dekart_graph.matrix:
            print(list)

        for index, pare in enumerate(dekart_graph.v_list):

            first = pare.sign[0] + pare.sign[1]
            second = pare.sign[2] + pare.sign[3]
            print(first, second)
            v1_next = self.find_next_v(self, first)
            v2_next = self.find_next_v(graph, second)
            if v1_next != None and v2_next != None:
                for new_index, new_pare in enumerate(dekart_graph.v_list):
                    new_first = new_pare.sign[0] + new_pare.sign[1]
                    new_second = new_pare.sign[2] + new_pare.sign[3]
                    if new_first != None and new_second != None:
                        if new_first == v1_next.sign and new_second == v2_next.sign:
                            print('find for', first, second,'-', new_first, new_second)
                            for m_index, list in enumerate(dekart_graph.matrix):
                                if m_index == index:
                                    for i in range(len(list)):
                                        if i == new_index:
                                            #list[i] += 1
                                            new_v_1 = first + second
                                            new_v_2 = new_first + new_second
                                            print(new_v_1, new_v_2)
                                            dekart_graph.add_e_oriented(new_v_1, new_v_2, '', 11)


        print('dekart')
        for list in dekart_graph.matrix:
            print(list)

        return dekart_graph.e_list

    def vector_multiplication(self, graph, dekart_graph):

        for v1 in graph.v_list:
            for v2 in self.v_list:
                new_v = v1.sign + v2.sign
                dekart_graph.add_v(new_v)
        for i in dekart_graph.v_list:
            print(i.sign)

        print(dekart_graph.v_amount)

        print('dekart')
        for list in dekart_graph.matrix:
            print(list)

        for index, pare in enumerate(dekart_graph.v_list):

            first = pare.sign[0] + pare.sign[1]
            second = pare.sign[2] + pare.sign[3]
            print(first, second)
            v1_next = self.find_next_v(self, first)
            v2_next = self.find_next_v(graph, second)
            if v1_next != None and v2_next != None:
                for new_index, new_pare in enumerate(dekart_graph.v_list):
                    new_first = new_pare.sign[0] + new_pare.sign[1]
                    new_second = new_pare.sign[2] + new_pare.sign[3]
                    if new_first != None and new_second != None:
                        if new_first == v1_next.sign and new_second == v2_next.sign:
                            print('find for', first, second,'-', new_first, new_second)
                            for m_index, list in enumerate(dekart_graph.matrix):
                                if m_index == index:
                                    for i in range(len(list)):
                                        if i == new_index:
                                            #list[i] += 1
                                            new_v_1 = first + second
                                            new_v_2 = new_first + new_second
                                            print(new_v_1, new_v_2)
                                            dekart_graph.add_e_oriented(new_v_1, new_v_2, '', 11)


        print('dekart')
        for list in dekart_graph.matrix:
            print(list)

        return dekart_graph.e_list



    def find_next_v(self, graph, vertex):
        for v in graph.v_list:
            if v.sign == vertex:
                for e in v.edges:
                    if e.vertex1 == v:
                        return e.vertex2