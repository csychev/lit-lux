
import json
from urllib.request import urlopen


class GoogleBooksClient:

    def __init__(self) -> None:
        self.base_url = "https://www.googleapis.com/books/v1"

    def book_search(query):

        url = self.base_url + "/volumes?q=" + query

        resp = urlopen(url)

        book_data = json.load(resp)

        return book_data
