from graph import*
from graph1 import*
from interface import MainScreen
from kivymd.app import MDApp
import os
from kivy.lang import Builder


class GraphApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = MainScreen()

    def build(self):
        return self.screen

#Builder.load_file(os.path.join(os.path.dirname(__file__), "graph.kv"))


if __name__ == '__main__':
    GraphApp().run()
    # g = Graph()
    # g.add_v('v1')
    # g.add_v('v2')
    # g.add_v('v3')
    # g.add_v('v4')
    # #g.add_v('v5')
    #
    #
    # g.add_e_oriented('v1','v2')
    # g.add_e_oriented('v2','v3')
    # g.add_e_not_oriented('v3', 'v4')
    # g.add_e_not_oriented('v4', 'v1')
    # g.print_matrix()
    #
    # print('--------')
    # print(g.min_path())
    # for v in g.v_list:
    #     print('----',v.sign,':')
    #     for i in v.degree:
    #         print(i.sign)
    #     print(len(v.edges))
    #     for i in v.edges:
    #         print(i.vertex1.sign,'->',i.vertex2.sign)
