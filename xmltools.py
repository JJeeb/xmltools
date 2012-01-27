import itertools
from collections import defaultdict
from xml.etree.ElementTree import Element

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
        if xmlElement.text and not xmlElement.text.isspace():
            d[tag].update({'#text': xmlElement.text})
    else:
        if xmlElement.text and not xmlElement.text.isspace():
            d[tag] = xmlElement.text
        else:
            d[tag] = None
    
    if hasChildren:
        children = defaultdict(list)
        for k, v in flatten(to_dict(c).items() for c in xmlElement):
            children[k].append(v)
        d[tag].update({ k: single(v) for k, v in children.items() })
    return d



def from_dict(d):
    tagname = d.keys()[0]
    element = Element(tagname)
    tagvalue = d[tagname]
    if type(tagvalue) is dict:
        for name, value in tagvalue.items():
            if name == '#text':
                element.text = value
            elif name[0] == '@':
                element.attrib[name[1:]] = value
            else:
                subElement = Element(tag=name)
                subElement.text = value
                element.append(subElement)
    else:
        element.text = d[tagname]
    return element

