import xml.dom.minidom as md


class FileRecordingSystem:
    def __init__(self):
        pass


    def record(self, graphs_list):
        # is called to record pets info into the file
        doc = md.Document()
        graph_info = doc.createElement('Graphs_list')
        doc.appendChild(graph_info)

        for item in graphs_list:
            graphs = doc.createElement('Graph')

            graph_name = doc.createElement('name')
            graph_name.appendChild(doc.createTextNode(item.name))

            v_amount = doc.createElement('vertexes_amount')
            v_amount.appendChild(doc.createTextNode(str(len(item.v_list))))

            v_list = ''
            for v in item.v_list:
                v_list += v.sign + ' '
            if v_list == '':
                v_list = '-'
            vertexes = doc.createElement('vertexes')
            vertexes.appendChild(doc.createTextNode(str(v_list)))


            v_colors = ''
            for v in item.v_list:
                if v.color != '':
                    v_colors += v.sign + '_' + v.color + ' '
            if v_colors == '':
                v_colors = '-'
            vertexes_colors = doc.createElement('vertexes_colors')
            vertexes_colors.appendChild(doc.createTextNode(str(v_colors)))

            v_text = ''
            for v in item.v_list:
                if v.text != '':
                    v_text += v.sign + '_' + v.text + ' '
            if v_text == '':
                v_text = '-'
            vertexes_text = doc.createElement('vertexes_text')
            vertexes_text.appendChild(doc.createTextNode(str(v_text)))

            o_e = ''
            n_e = ''
            for e in item.e_list:
                if e.type == 1:
                    o_e += e.sign + ':' + e.vertex1.sign + '_' + e.vertex2.sign + ' '
                elif e.type == 2:
                    n_e += e.sign + ':' + e.vertex1.sign + '_' + e.vertex2.sign + ' '
            if o_e == '':
                o_e = '-'
            if n_e == '':
                n_e = '-'

            o_edges = doc.createElement('oriented_edges')
            o_edges.appendChild(doc.createTextNode(o_e))

            n_edges = doc.createElement('not_oriented_edges')
            n_edges.appendChild(doc.createTextNode(n_e))

            e_colors = ''
            for e in item.e_list:
                if e.color != '':
                    e_colors += e.sign + '_' + e.color + ' '
            if e_colors == '':
                e_colors = '-'
            edges_colors = doc.createElement('edges_colors')
            edges_colors.appendChild(doc.createTextNode(str(e_colors)))

            #
            # phone = doc.createElement('phone_number')
            # phone.appendChild(doc.createTextNode(item['phone_number']))
            #
            # mail = doc.createElement('mail')
            # mail.appendChild(doc.createTextNode(item['mail']))
            #
            # address = doc.createElement('handler_address')
            # address.appendChild(doc.createTextNode(item['handler_address']))

            graphs.appendChild(graph_name)
            graphs.appendChild(v_amount)
            #graphs.appendChild(matrix)
            graphs.appendChild(vertexes)
            graphs.appendChild(vertexes_colors)
            graphs.appendChild(vertexes_text)
            graphs.appendChild(o_edges)
            graphs.appendChild(n_edges)
            graphs.appendChild(edges_colors)

            # pet.appendChild(mail)
            # pet.appendChild(address)

            graph_info.appendChild(graphs)

        file = open('graphs.xml', 'w')
        doc.writexml(file, encoding='windows-1251')
        file.close()

    def read(self):
        pass