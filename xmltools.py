import itertools
from xml.etree.ElementTree import Element

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
    element = Element(tag=d['#tag'])
    if '#text' in d:
        element.text = d['#text']
    if '@attributes' in d:
        element.attrib = d['@attributes'].copy()
    if '#children' in d:
        element.extend([from_dict(c) for c in d['#children']])
    return element
