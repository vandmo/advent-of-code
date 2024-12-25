from typing import Literal
from xml.sax.saxutils import escape, quoteattr

_HEADER = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<graphml
 xmlns="http://graphml.graphdrawing.org/xmlns"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xmlns:y="http://www.yworks.com/xml/graphml"
 xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns http://www.yworks.com/xml/schema/graphml/1.1/ygraphml.xsd">
  <key for="node" id="d6" yfiles.type="nodegraphics"/>
  <key for="edge" id="d10" yfiles.type="edgegraphics"/>
  <key id="edge_weight" for="edge" attr.name="weight" attr.type="double" />
  <graph edgedefault="directed" id="G">
"""

_NODE = """    <node id={id_attr}>
      <data key="d6">
        <y:ShapeNode>
          <y:Geometry height="{height}" width="{width}" x="{x}" y="{y}"/>
          <y:Fill color={color} transparent="false"/>
          <y:BorderStyle color="#000000" raised="false" type="line" width="1.0"/>
          <y:NodeLabel alignment="center" autoSizePolicy="content" fontFamily="Dialog" fontSize="12" fontStyle="plain" hasBackgroundColor="false" hasLineColor="false" height="20.344114303588867" horizontalTextPosition="center" iconTextGap="4" modelName="custom" textColor="#000000" verticalTextPosition="bottom" visible="true" width="11.800048828125" x="9.0999755859375" y="4.827942848205566">{label}<y:LabelModel>
              <y:SmartNodeLabelModel distance="4.0"/>
            </y:LabelModel>
            <y:ModelParameter>
              <y:SmartNodeLabelModelParameter labelRatioX="0.0" labelRatioY="0.0" nodeRatioX="0.0" nodeRatioY="0.0" offsetX="0.0" offsetY="0.0" upX="0.0" upY="-1.0"/>
            </y:ModelParameter>
          </y:NodeLabel>
          <y:Shape type="{form}"/>
        </y:ShapeNode>
      </data>
    </node>
"""

_FOOTER = "  </graph>\n</graphml>"


class Graph:
    def __init__(self):
        self._nodes = dict()
        self._edges = []

    def add_node(
        self,
        id,
        *,
        form: Literal["ellipse", "star", "rectangle", "diamond"] = "rectangle",
        size=1.0,
        color="#FFCC00",
        label=None,
    ):
        assert form in ["ellipse", "star", "rectangle", "diamond"]
        self._nodes[id] = (form, size, color, label if label is not None else id)

    def add_edge(self, source, target, *, weight=None, width=1.0, color="#000000"):
        self._edges.append((source, target, weight, width, color))

    def __str__(self):
        s = _HEADER
        for idx, (id, (form, size, color, label)) in enumerate(self._nodes.items()):
            s += _NODE.format(
                id_attr=quoteattr(id),
                label=escape(label),
                form=form,
                x=(idx % 10) * 50,
                y=(idx // 10) * 50,
                width=size * 30.0,
                height=size * 30.0,
                color=quoteattr(color),
            )
        for source, target, weight, width, color in self._edges:
            s += f"    <edge source={quoteattr(source)} target={quoteattr(target)}>\n"
            if weight is not None:
                s += f"""      <data key="edge_weight">{escape(str(weight))}</data>\n"""
            s += f"""      <data key="d10">
        <y:PolyLineEdge>
          <y:Path sx="0.0" sy="0.0" tx="0.0" ty="0.0"/>
          <y:LineStyle color={quoteattr(color)} type="line" width="{width}"/>
          <y:Arrows source="none" target="standard"/>
          <y:BendStyle smoothed="false"/>
        </y:PolyLineEdge>
      </data>
    </edge>\n"""
        s += _FOOTER
        return s

    @staticmethod
    def from_edges(edges, form="rectangle"):
        """edges is a collection of tuples with (source, edge, weight)"""
        graph = Graph()
        for edge in edges:
            assert 2 <= len(edge) <= 3
            source = str(edge[0])
            target = str(edge[1])
            graph.add_node(source, form)
            graph.add_node(target, form)
            if len(edge) > 2:
                graph.add_edge(source, target, edge[2])
            else:
                graph.add_edge(source, target)
        return graph
