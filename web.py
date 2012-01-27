from pymongo import Connection
import sys
import xmltools
from xml.etree.ElementTree import parse
from flask import Flask
import json

app = Flask(__name__)
db = Connection().test

@app.route('/year/<year>')
def findBookByYear(year):
    return json.dumps(list(db.books.find({'year': year}, {'_id': 0})))



if __name__ == '__main__':
    db.books.remove()
    xml = parse(sys.argv[1]) 
    for book in xmltools.to_dict(xml.getroot())['bookstore']['book']:
        db.books.insert(book)

    app.run(debug=True)

