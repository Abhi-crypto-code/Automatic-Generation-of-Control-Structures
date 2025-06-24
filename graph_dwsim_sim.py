import xml.etree.ElementTree as ET
import networkx as nx
import re


cnt = 1
# --- CONFIG ---
INPUT_XML   = "DWSIM_files/maleic_anhydride.xml"
OUTPUT_GML  = "DWSIM_files/flowsheet.graphml"

# --- PARSE XML ---
tree = ET.parse(INPUT_XML)
root = tree.getroot()

# --- BUILD GRAPH ---
G = nx.DiGraph()
id_to_name = {}
for go in root.findall(".//GraphicObject"):
    guid = go.findtext("Name")
    tag  = go.findtext("Tag") or guid

    if not tag:                              # if it’s now empty, fall back
        tag = guid

        
    print(f"{cnt} : {tag} ")
    cnt+=1
     # store it for lookups
    id_to_name[guid] = tag


    tag = tag.split('-')[0]
    # **Use the GraphML‐standard key "name" rather than "label"**
    G.add_node(guid,label = tag)

    # edges: from any AttachedFromObjID → this object
    for conn in go.findall(".//InputConnectors/Connector"):
        src = conn.get("AttachedFromObjID")
        if src:
            G.add_edge(src, guid)

    # edges: from this object → any AttachedToObjID
    for conn in go.findall(".//OutputConnectors/Connector"):
        dst = conn.get("AttachedToObjID")
        if dst:
            G.add_edge(guid, dst)

# --- WRITE OUT ---
nx.write_graphml(G, OUTPUT_GML)
print(f"Saved graph with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges to '{OUTPUT_GML}'")
