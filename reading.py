from fastapi import APIRouter, HTTPException
from fastapi.params import Path
from starlette import status
from data import READING, BOOKS


router = APIRouter(
    prefix = '/reading',
    tags = ['reading']
)




@router.get("/")
async def fetch_all_reading():
    """
        Retrieves a list of all books you are currently reading in your library.

        Returns:
            list: A list of dictionaries representing Reading objects.
    """
    return READING


@router.put("/update_current_page/{book_id}/{current_page}")
async def update_current_page(book_id: int, current_page: int):
    """
        Updates the current page number for a book in your "Currently Reading" list.

        Args:
            book_id (int): Unique identifier for the book you're reading.
            current_page (int): The new page number you've reached in the book.
    """
    target_book = None

    for book in BOOKS:
        if book.id == book_id:
            target_book = book
            break

    if target_book is None:
        return

    target_read = None
    for read in READING:
        if read.book_id == book_id:
            target_read = read
            break

    if target_read is None:
        return

    if current_page > target_book.pages:
        return

    if current_page == target_book.pages:
        target_book.status = 'read'
        READING.remove(target_read)
    else:
        target_read.current_page = current_page
        target_read.progress = current_page / target_book.pages
