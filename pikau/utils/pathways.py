import pygraphviz as pgv
from pikau.models import PikauCourse

GRAPH_TEMPLATE = (
    "digraph {{"
    "graph [bgcolor=transparent,fontname=inherit];"
    "node [shape=box,fillcolor=white,style=filled,fontname=inherit];"
    "{nodes}"
    "{edges}"
    "}}"
)
NODE_TEMPLATE = "{id} [label=\"{name}\", href=\"{url}\"];"
EDGE_TEMPLATE = "{start_id} -> {end_id};"

def create_pathways_notation():
    """ TODO """
    all_pikau = PikauCourse.objects.all()

    # Create nodes
    nodes = []
    for pikau in all_pikau:
        node = NODE_TEMPLATE.format(
            id=pikau.id,
            name=pikau.__str__(),
            url=pikau.get_absolute_url(),
        )
        nodes.append(node)
    # Create edges
    edges = []
    for pikau in all_pikau:
        for prereq in pikau.prerequisites.all():
            edge = EDGE_TEMPLATE.format(
                start_id=prereq.id,
                end_id=pikau.id,
            )
            edges.append(edge)

    print(nodes)
    print(edges)
    # Create graph
    graph = GRAPH_TEMPLATE.format(
        nodes="".join(nodes),
        edges="".join(edges),
    )
    return graph
