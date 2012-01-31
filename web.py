from pymongo import Connection
import sys
import xmltools
from xml.etree.ElementTree import parse, Element, tostring
from flask import Flask
import xmltools

app = Flask(__name__)
db = Connection().test

@app.route('/year/<year>')
def findBookByYear(year):
    booksByYear = db.books.find({'#children': {'$elemMatch': {'#tag': 'year', '#text': year}}})
    root = Element(tag='books')
    root.extend(xmltools.from_dict(b) for b in booksByYear)
    return tostring(root)


if __name__ == '__main__':
    db.books.remove()
    xml = parse(sys.argv[1]) 
    d = xmltools.to_dict(xml.getroot())
    for book in xmltools.to_dict(xml.getroot())['#children']:
        db.books.insert(book)

    app.run(debug=True)

