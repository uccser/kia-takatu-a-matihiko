"""Module for creating pikau course pathways."""

from pikau.models import PikauCourse, READINESS_LEVELS
from django.db.models import Q, Count


GRAPH_TEMPLATE = (
    "digraph {{"
    'graph [bgcolor=transparent,fontname="helvetica"];'
    'node [shape=box,fillcolor=white,style=filled,fontname="helvetica", margin=0.1];'
    "{nodes}"
    "{edges}"
    "}}"
)
NODE_TEMPLATE = "{id} [label=\"{name}\", href=\"{url}\", color=\"{color}\", penwidth={penwidth}.0];"
EDGE_TEMPLATE = "{start_id} -> {end_id};"


def create_pathways_notation():
    """Create Graphviz graph notation.

    Returns:
        String of graph notation.
    """
    all_pikau = PikauCourse.objects.annotate(Count("postrequisites")).filter(
        Q(readiness_level__isnull=False) | Q(postrequisites__count__gt=0)
    )

    # Create nodes
    nodes = []
    for pikau in all_pikau:
        if pikau.readiness_level in READINESS_LEVELS:
            color = READINESS_LEVELS[pikau.readiness_level]["color"]
            pen_width = 4
        else:
            color = "#444444"
            pen_width = 2
        node = NODE_TEMPLATE.format(
            id=pikau.id,
            name=pikau.__str__(),
            url=pikau.get_absolute_url(),
            color=color,
            penwidth=pen_width,
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

    # Create graph
    graph = GRAPH_TEMPLATE.format(
        nodes="".join(nodes),
        edges="".join(edges),
    )
    return graph
