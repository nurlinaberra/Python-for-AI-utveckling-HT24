class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

# Create an instance of the Book class
book1 = Book("Python Programming", "Nurlin", 300)

# Display information about the book
book1.display_info()

print("\nBook 2:")
book2.display_info()