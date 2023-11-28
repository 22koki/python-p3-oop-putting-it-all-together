# lib/book.py

class Book:
    def __init__(self, title, page_count, publication_year):
        self.title = title
        self._page_count = page_count  # Change the name to _page_count
        self.publication_year = publication_year

    def get_info(self):
        return f"{self.title} by ({self.publication_year}), {self._page_count} pages"

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value
