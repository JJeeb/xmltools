import itertools
from collections import defaultdict

def single(lst):
    return lst[0] if len(lst) == 1 else lst 


def flatten(lst):
    return itertools.chain(*lst)

def to_dict(xmlElement):
    d = {}
    tag = xmlElement.tag
    hasChildren = len(xmlElement) != 0

    if xmlElement.attrib or hasChildren:
        d[tag] = { '@' + name : value for name, value in xmlElement.attrib.items() }
        if xmlElement.text:
            d[tag].update({'#text': xmlElement.text})
    else:
        d[tag] = xmlElement.text
    
    if hasChildren:
        children = defaultdict(list)
        for k, v in flatten(to_dict(c).items() for c in xmlElement):
            children[k].append(v)
        d[tag].update({ k: single(v) for k, v in children.items() })
    return d
