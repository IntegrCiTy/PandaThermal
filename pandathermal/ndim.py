import numpy as np
import networkx as nx


def create_empty_directed_network():
    return nx.DiGraph()


def add_srce(g, name):
    return _add_node(g, name, type="SRCE")


def add_node(g, name):
    return _add_node(g, name)


def add_nodes_from(g, names):
    return [add_node(g, n) for n in names]


def add_sink(g, name, p_kw):
    return _add_node(g, name, p_kw=p_kw, type="SINK")


def _add_node(g, name, p_kw=0.0, type="NODE"):
    g.add_node(name, p_kw=p_kw, type=type)
    return name


def add_pipe(g, from_node, to_node):
    g.add_edge(from_node, to_node)
    return from_node, to_node


def add_pipes_from(g, pipes):
    return [add_pipe(g, p[0], p[1]) for p in pipes]


def compute_pipes_diameter(g, dt, v_max=2.0, f_sim=0.8, cp=4.186):
    desc = {src: [src] + list(nx.descendants(g, src)) for src in g.nodes}
    attr = {src: [nx.get_node_attributes(g, "p_kw")[n] for n in d_set] for src, d_set in desc.items()}
    node = {src: sum(list(d_att)) for src, d_att in attr.items()}
    pipe = {e: min(node[e[0]], node[e[1]]) for e in g.edges}
    return {k: round(2*np.sqrt(f_sim*p_kw/(np.pi*v_max*cp*dt)), 2) for k, p_kw in pipe.items()}
