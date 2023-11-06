# isbn.py

import requests

def getISBN(isbn):
    api_url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}'
    response = requests.get(api_url)
    data = response.json()
    # print(data)
    book_info = {
        'title': data["items"][0]["volumeInfo"]["title"],
        'authors': data["items"][0]["volumeInfo"].get("authors", []),
        'publisher': data["items"][0]["volumeInfo"].get("publisher", "Bilinmiyor"),
        'publication_date': data["items"][0]["volumeInfo"].get("publishedDate", "Bilinmiyor"),
        'page_count': data["items"][0]["volumeInfo"].get("pageCount", []),
        'language': data["items"][0]["volumeInfo"].get("language", "Bilinmiyor"),
        'description': data["items"][0]["volumeInfo"].get("description", ""),
        'smallThumbnail': data["items"][0]["volumeInfo"].get("imageLinks", {}).get("smallThumbnail", "Resim Yok"),
        'isbn': isbn
    }
    return book_info


def get_book_cover_url(isbn):
    base_url = "http://openlibrary.org/api/books"
    response = requests.get(f"{base_url}?bibkeys=ISBN:{isbn}&format=json&jscmd=data")

    if response.status_code == 200:
        data = response.json()
        if f"ISBN:{isbn}" in data:
            book_info = data[f"ISBN:{isbn}"]
            if "cover" in book_info:
                cover_url = book_info["cover"]["medium"]
                return cover_url
            else:
                return "img/kutuphane.png"
        else:
            return "img/kutuphane.png"
    else:
        return "img/kutuphane.png"

# print(getISBN("9786059129329"))

