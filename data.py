
class Book:
    """
        Represents a book in the library.

        Attributes:
            id (int): Unique identifier for the book.
            title (str): Title of the book.
            author (str): Author of the book.
            synopsis (str): Short summary of the book.
            isbn (str): International Standard Book Number.
            status (str): Current reading status (e.g., unread, reading, read).
            pages (int): Total number of pages in the book.
            genre (str): Genre of the book.
    """
    def __init__(self, id, title, author, synopsis, isbn, status, pages, genre):
        self.id = id
        self.title = title
        self.author = author
        self.synopsis = synopsis
        self.isbn = isbn
        self.status = status
        self.pages = pages
        self.genre = genre

BOOKS = [Book(1, "APIs: A Strategy Guide", "Daniel Jacobson", "Creating channels with application programming interfaces", "9781449308926", "unread", 149, "Computers"),
         Book(2, "The Lord of the Rings", "J. R. R. Tolkien", "Presents the epic depicting the Great War of the Ring, a struggle between good and evil in Middle-earth, following the odyssey of Frodo the hobbit and his companions on a quest to destroy the Ring of Power.", "9780544003415", "unread", 1178, "Fiction")]

class Note:
    """
        Represents a note associated with a book in the library.

        Attributes:
            id (int): Unique identifier for the note.
            book_id (int): Foreign key referencing the book this note belongs to.
            content (str): The actual note content.
            page_num (int): The page number in the book where the note is associated with.
            created_at (datetime): Date and time when the note was created.
            updated_at (datetime): Date and time when the note was last updated.
    """

    def __init__(self, id, book_id, content, page_num, created_at, updated_at):
        self.id = id
        self.book_id = book_id
        self.content = content
        self.page_num = page_num
        self.created_at = created_at
        self.updated_at = updated_at


class Reading:
    """
        Represents a book that is currently being read, including the user's progress.

        Attributes:
            book_id (int): Unique identifier for the book being read.
            current_page (int): The current page the user has reached in the book.
            progress (float): The user's progress in the book, calculated as a percentage (0.0 to 1.0).
    """
    def __init__(self, book_id, current_page):
        self.book_id = book_id
        self.current_page = current_page

        for book in BOOKS:
            if book.id == book_id:
                self.progress = current_page / book.pages
                break


NOTES = []
READING = []

# 9780786490653
# 9781487523909
# 9781449308926
# 9780544003415
# 9798886630435
# 9780593331279
# 1449494943

