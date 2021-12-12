import urllib.parse
import flask
from flask import Flask, request
from urllib.request import urlopen
import json

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/books/search", methods=['GET', 'POST'])
def search_info():
    query = request.args.get('q')
    book_dict = {
        "title": "",
        "author": "",
        "page_count": "",
        "publication_date": "",
        "category": ""

    }
    api = 'https://www.googleapis.com/books/v1/volumes?q='

    safe_query = urllib.parse.quote_plus(query)
    resp = urlopen(api + safe_query)

    book_data = json.load(resp)

    volume_info = book_data["items"][0]["volumeInfo"]
    author = volume_info["authors"]
    prettify_author = author if len(author) > 1 else author[0]

    book_dict["title"] = volume_info['title']
    book_dict["author"] = prettify_author
    book_dict["page_count"] = volume_info["pageCount"]
    book_dict["publication_date"] = volume_info["publishedDate"]
    book_dict["category"] = volume_info["categories"]

    return book_dict


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
