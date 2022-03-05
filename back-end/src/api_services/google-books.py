import urllib.parse
import flask
from flask import Flask, request
from urllib.request import urlopen
import json
from flask_cors import CORS, cross_origin
import urllib.parse

app = Flask(__name__)
app.config['CORS_HEADERS'] = "Content-Type"
cors = CORS(app)


@app.route("/books/search", methods=['GET'])
@cross_origin()
def search_info():
    query = request.args.get('q')
    book_dict = {
        "title": "",
        "author": "",
        "page_count": "",
        "publication_date": "",
        "category": "",
        "summary": ""
    }
    api = 'https://www.googleapis.com/books/v1/volumes?q='

    # safe_query = urllib.parse.quote_plus(query)
    print("LOOK HERE >>> ", api+query)
    encoded_query = urllib.parse.quote(query)
    resp = urlopen(api+encoded_query)
    print(resp)

    book_data = json.load(resp)

    volume_info = book_data["items"][0]["volumeInfo"]
    author = volume_info["authors"]
    prettify_author = author if len(author) > 1 else author[0]

    book_dict["title"] = volume_info['title']
    book_dict["author"] = prettify_author
    book_dict["page_count"] = volume_info["pageCount"]
    book_dict["publication_date"] = volume_info["publishedDate"]
    book_dict["category"] = volume_info["categories"]
    book_dict["summary"] = volume_info["description"]
    # print(book_dict["summary"])
    return book_dict, 200


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
