class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_pages(self):
        return self.pages

    def __repr__(self):
        return f"{self.title} by {self.author}, {self.pages} pages"


book = Book("War and Peace", "Leo Tolstoy", 1225)
print(book.get_title())  # "War and Peace"
print(book.get_author())  # "Leo Tolstoy"
print(book.get_pages())  # 1225
print(book)  # "War and Peace by Leo Tolstoy, 1225 pages"

'''Create a class called Book that has three instance variables: title, author, and pages. The class should have the
 following methods:

__init__(self, title, author, pages): This is the constructor for the class. It should initialize the title, author,
and pages instance variables.
get_title(self): This method should return the title of the book
get_author(self): This method should return the author of the book
get_pages(self): This method should return the number of pages of the book
__str__(self): This method should return a string representation of the book in the following format: "title by author,
pages pages"
Here's an example of how the class should be used:'''
