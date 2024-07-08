from fastapi import HTTPException, APIRouter
from fastapi.params import Path, Query
import requests
from random import randint
from starlette import status
from data import READING, NOTES, BOOKS, Reading, Book

router = APIRouter(
    prefix = '/books',
    tags = ['books']
)

async def fetch_book_data_by_isbn(book_isbn: str):
    """
    Fetches book data from Google Books API using the provided ISBN.

    Args:
        book_isbn (str): International Standard Book Number of the book.

    Raises:
        HTTPException: If the book with the provided ISBN is not found (404 Not Found).

    Returns:
        dict: A dictionary containing book data from Google Books API.
    """
    url = "https://www.googleapis.com/books/v1/volumes?q=isbn:" + book_isbn
    result = requests.get(url).json()
    if result['totalItems'] == 0:
        raise HTTPException(status_code=404, detail='Book ISBN not found')
    return result['items'][0]

def get_next_book_id():
    """
    Generates the next available ID for a new book.

    Returns:
        int: The next unique ID for a book.
    """

    return 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1

def create_book_from_json(book_json):
    """
    Creates a new Book object from a JSON dictionary containing book data.

    Args:
        book_json (dict): A dictionary containing book data in a format expected from the Google Books API.

    Returns:
        Book: A new Book object populated with data extracted from the provided JSON.

    Raises:
        KeyError: If any required keys are missing from the provided JSON data.
    """

    id = get_next_book_id()

    try:
        title = book_json['volumeInfo']['title']
        author = book_json['volumeInfo']['authors'][0]
        synopsis = book_json['volumeInfo']['description']
        isbn = book_json['volumeInfo']['industryIdentifiers'][0]['identifier']
        pages = book_json['volumeInfo']['pageCount']
        genre = book_json['volumeInfo']['categories'][0]
    except KeyError as e:
        raise KeyError(f"Missing required key: {e}") from e  # Re-raise with informative message

    status = "unread"

    return Book(id, title, author, synopsis, isbn, status, pages, genre)

@router.get("/")
async def fetch_all_books():
    """
        Retrieves a list of all books currently stored in your library.

        Returns:
            list: A list of dictionaries representing Book objects.
    """
    pass

@router.get("/fetch_by_id")
async def fetch_book_by_id(book_id: int):
    """
        Retrieves a specific book from your library by its unique ID.

        Args:
            book_id (int): Unique identifier for the book to be retrieved.

        Returns:
            list: A list representing the Book object with the matching ID.
    """
    pass

@router.get("/fetch_by_status")
async def fetch_book_by_status(book_status: str):
    """
        Retrieves a list of books from your library that have a specific status.

        Args:
            book_status (str): The status to filter by (e.g., "unread", "reading", "read").

        Returns:
            list: A list of dictionaries representing Book objects with the matching status.
    """
    pass

@router.get("/fetch_by_author")
async def fetch_book_by_author(book_author: str):
    """
        Retrieves a list of books from your library written by a specific author.

        Args:
            book_author (str): The author's name to filter by.

        Returns:
            list: A list of dictionaries representing Book objects written by the specified author.
    """
    pass

@router.delete("/delete/{book_id}")
async def delete_book_by_id(book_id: int):
    """
        Deletes a book from your library by its unique ID.

        Args:
            book_id (int): Unique identifier for the book to be deleted.
    """
    for read in READING:
        if read.book_id == book_id:
            READING.remove(read)
            break

    notes_to_remove = []
    for i in range(len(NOTES)):
        if NOTES[i].book_id == book_id:
            notes_to_remove.append(i)

    for i in notes_to_remove:
        NOTES.pop(i)

    for book in BOOKS:
        if book.id == book_id:
            BOOKS.remove(book)
            break

@router.put("/update_status/{book_id}/{book_new_status}")
async def update_book_status(book_id: int, book_new_status: str):
    """
        Updates the status of a book in your library. asdadasdas

        Args:
            book_id (int): Unique identifier for the book to be updated.
            book_new_status (str): The new status for the book (e.g., "unread", "reading", "read").
    """
    pass

@router.post("/add_by_isbn/{book_isbn}")
async def add_book_by_isbn(book_isbn: str):
    """
        Adds a new book to your library by searching for it using the provided ISBN number.

        Args:
            book_isbn (str): The ISBN number of the book to be added.

        Raises:
            Exception: If the ISBN lookup fails or the book already exists in your library.
    """
    book_json = await fetch_book_data_by_isbn(book_isbn)
    book = create_book_from_json(book_json)
    BOOKS.append(book)
