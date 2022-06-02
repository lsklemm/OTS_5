import xml.sax


class FileReadingSysytem(xml.sax.ContentHandler):
    def __init__(self):
        self.graph_name = False
        self.vertexes = False
        self.vertexes_colors = False
        self.vertexes_text = False
        self.oriented_edges = False
        self.not_oriented_edges = False
        self.edges_colors = False


        # self.edges_colors = False
        # self.phone_number = False
        # self.mail = False
        # self.handler_address = False


        self.count = 0
        # self.count_handler = 0
        # self.bad_files_count = 0





    def startElement(self, name, attrs):
        self.current_data = name
        if self.current_data == 'Graphs_list':
            self.graphs_list = []
            # self.handlers_list = []
            # self.all_list = []
            # self.bad_line_name = ''
            # self.bad_line_count = 0
            self.line = 1

            self.graph_name_line = False
            self.vertexes_line = False
            self.vertexes_text_line = False
            self.vertexes_colors_line = False
            self.edges_colors_line = False
            self.oriented_edges_line = False
            self.not_oriented_edges_line = False
            # self.phone_number_line = False
            # self.mail_line = False
            # self.handler_address_line = False
            # self.not_oriented_edges_line = False

            # self.name_line_count = 0
            # self.vertexes_line_count = 0
            # self.vertexes_colors_line_count = 0
            # self.vertexes_text_line_count = 0
            # self.oriented_edges_line_count = 0
            # self.not_oriented_edges_line_count = 0
            # self.edges_colors_line_count = 0
            # self.phone_number_line_count = 0
            # self.mail_line_count = 0
            # self.handler_address_line_count = 0


        elif self.current_data == 'Graph':
            self.graph = {}
            # self.handler = {}
            # self.all = {}
            self.line += 1

            self.close_graph_name = False
            self.close_vertexes = False
            self.close_vertexes_colors = False
            self.close_vertexes_text = False
            self.close_oriented_edges = False
            self.close_not_oriented_edges = False
            self.close_edges_colors = False
            # self.close_phone_number = False
            # self.close_mail = False
            # self.close_handler_address = False



        elif self.current_data == 'name':
            self.name=True
            self.line += 1
            #self.name_line_count = self.line

        elif self.current_data == 'vertexes':
            self.vertexes=True
            self.line += 1
            #self.vertexes_line_count = self.line

        elif self.current_data == 'vertexes_colors':
            self.vertexes_colors = True
            self.line += 1
            #self.vertexes_colors_line_count = self.line

        elif self.current_data == 'vertexes_text':
            self.vertexes_text = True
            self.line += 1
            #self.vertexes_text_line_count = self.line

        elif self.current_data == 'oriented_edges':
            self.oriented_edges = True
            self.line += 1
            #self.oriented_edges_line_count = self.line

        elif self.current_data == 'not_oriented_edges':
            self.not_oriented_edges = True
            self.line += 1
            #self.not_oriented_edges_line_count = self.line


        elif self.current_data == 'edges_colors':
            self.edges_colors = True
            self.line += 1
            #self.edges_colors_line_count = self.line
        # elif self.current_data == 'phone_number':
        #     self.phone_number = True
        #     self.line += 1
        #     self.phone_number_line_count = self.line
        # elif self.current_data == 'mail':
        #     self.mail = True
        #     self.line += 1
        #     self.mail_line_count = self.line
        # elif self.current_data == 'handler_address':
        #     self.handler_address = True
        #     self.line += 1
        #     self.handler_address_line_count = self.line
        # 

        self.current_data=''


    def endElement(self, tag):
        if tag == 'name':
            if self.name_line == True:
                self.name_line = False
                self.close_name = True
        elif tag == 'vertexes':
            if self.vertexes_line == True:
                self.vertexes_line = False
                self.close_vertexes = True
        elif tag == 'vertexes_colors':
            if self.vertexes_colors_line == True:
                self.vertexes_colors_line = False
                self.close_vertexes_colors = True
        elif tag == 'vertexes_text':
            if self.vertexes_text_line == True:
                self.vertexes_text_line = False
                self.close_vertexes_text = True
        elif tag == 'oriented_edges':
            if self.oriented_edges_line == True:
                self.oriented_edges_line = False
                self.close_oriented_edges = True

        elif tag == 'not_oriented_edges':
            if self.not_oriented_edges_line == True:
                self.not_oriented_edges_line = False
                self.close_not_oriented_edges = True

        elif tag == 'edges_colors':
            if self.edges_colors_line == True:
                self.edges_colors_line = False
                self.close_edges_colors = True
        # elif tag == 'phone_number':
        #     if self.phone_number_line == True:
        #         self.phone_number_line = False
        #         self.close_phone_number = True
        # elif tag == 'mail':
        #     if self.mail_line == True:
        #         self.mail_line = False
        #         self.close_mail = True
        # elif tag == 'handler_address':
        #     if self.handler_address_line == True:
        #         self.handler_address_line = False
        #         self.close_handler_address = True



        elif tag == 'Graph':
            self.line += 1

            self.graphs_list.append(self.graph)
            self.graph = {}
            self.count=0
            

    def characters(self, content):
        # pet info
        if self.name:
            #self.name = content
            self.graph['name'] = content
            self.count += 1
            self.name = False
            self.name_line = True

        elif self.vertexes:
            self.graph['vertexes'] = content

            self.count += 1
            self.vertexes = False
            self.vertexes_line = True

        elif self.vertexes_colors:
            self.vertexes_colors_line = True
            self.count += 1
            self.graph['vertexes_colors'] = content
            self.vertexes_colors = False


        elif self.vertexes_text:
            self.graph['vertexes_text'] = content

            self.vertexes_text = False
            self.vertexes_text_line = True

            self.count += 1

        elif self.oriented_edges:
            self.graph['oriented_edges'] = content

            self.oriented_edges = False
            self.oriented_edges_line = True

            self.count += 1


        elif self.not_oriented_edges:
            self.graph['not_oriented_edges'] = content

            self.not_oriented_edges = False
            self.not_oriented_edges_line = True

            self.count += 1


        # handler info
        elif self.edges_colors:
            self.graph['edges_colors'] = content

            self.edges_colors = False
            self.edges_colors_line = True
            #self.count_handler += 1

        # elif self.phone_number:
        #     self.handler['phone_number'] = content
        #     self.all['phone_number'] = content
        #     self.phone_number = False
        #     self.phone_number_line = True
        #     self.count_handler += 1
        # elif self.mail:
        #     self.handler['mail'] = content
        #     self.all['mail'] = content
        #     self.mail_line = True
        #     self.mail = False
        #     self.count_handler += 1
        # elif self.handler_address:
        #     self.handler_address_line = True
        #     self.handler['handler_address'] = content
        #     self.all['handler_address'] = content
        #     self.handler_address = False
        #     self.count_handler += 1

           #self.not_oriented_edges = content

    def return_graphs_list(self):
        return self.graphs_list

