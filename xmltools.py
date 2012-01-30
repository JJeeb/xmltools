import itertools
from collections import defaultdict
from xml.etree.ElementTree import Element

def single(lst):
    return lst[0] if len(lst) == 1 else lst 


def flatten(lst):
    return itertools.chain(*lst)


def to_dict(xmlElement):
    d = {'#tag': xmlElement.tag}
    if xmlElement.text and  not xmlElement.text.isspace():
        d.update({'#text': xmlElement.text})
    if xmlElement.attrib:
        d.update({'@attributes': xmlElement.attrib.copy()}) 
    if len(xmlElement) != 0:
        d.update({'#children': [to_dict(c) for c in xmlElement]})

    return d



def from_dict(d):

    def go(element, value):
        if type(value) is str:
            element.text = value
        elif type(value) is list:
            for child_value in value:
                element.append(go(Element(tag=child_name), child_value))
        elif type(value) is dict:
            element.attrib = {name[1:]: value for name, value in value.items() if name[0] == '@'}
            element.text = value['#text'] if '#text' in value else None

            children = {name: value for name, value in value.items() if name[0] != '@' and name != '#text' }
            for child_name, child_value in children.items():
                element.append(go(Element(tag=child_name), child_value))
        return element

    tagname = d.keys()[0]
    return go(Element(tag=tagname), d[tagname])

