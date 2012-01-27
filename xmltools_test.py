import xmltools
import unittest
from xml.etree.ElementTree import XML


class ToDictTest(unittest.TestCase):

    def test_todict(self):
        self.assert_todict('<e/>', {'e': None})
        self.assert_todict('<e>text</e>', {'e': 'text'})
        self.assert_todict('<e name="value" id="12"/>', {'e': {'@name': 'value', '@id': '12'}})
        self.assert_todict('<e name="value">foo</e>', {'e': {'@name': 'value', '#text': 'foo'}})
        self.assert_todict('<e><a>foo</a><b>bar</b></e>', {'e': {'a': 'foo', 'b': 'bar'}})
        self.assert_todict('<e><a>foo</a><a>bar</a></e>', {'e': {'a': ['foo', 'bar']}})
        self.assert_todict('<e>foo<a>bar</a></e>', {'e': {'a': 'bar', '#text':'foo'}})

    def test_no_blank_text(self):
        self.assert_todict('<e>\n</e>', {'e': None})

    def assert_todict(self, s, expected):
        self.assertEquals(xmltools.to_dict(XML(s)), expected)

