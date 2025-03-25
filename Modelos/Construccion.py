import graphviz

def mostrarAFND(automata):
    automataGrafico = graphviz.Digraph()

    for transicion in automata.transiciones:
        automataGrafico.edge(tail_name="q"+transicion.origen.nombre,head_name="q"+transicion.destino.nombre,label=transicion.simbolo)


    automataGrafico.node_attr['shape'] = 'circle'
    automataGrafico.node_attr['color'] = 'lightblue'
    automataGrafico.node_attr['size'] = '1.5'
    automataGrafico.edge_attr['width'] = '2.0'
    automataGrafico.view()
