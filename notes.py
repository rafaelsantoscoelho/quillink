import datetime
from datetime import datetime

from fastapi import APIRouter, HTTPException
from fastapi.params import Path
from starlette import status

from data import BOOKS, NOTES, READING, Note

router = APIRouter(
    prefix = '/notes',
    tags = ['notes']
)



def get_next_note_id():
    """
        Generates the next available ID for a new note.

        Returns:
            int: The next unique ID for a note.
    """
    return 1 if len(NOTES) == 0 else NOTES[-1].id + 1

@router.get("/")
async def fetch_all_notes():
    """
        Retrieves a list of all notes currently stored in the library.

        Returns:
            list: A list of dictionaries representing Note objects.
    """
    return NOTES

@router.post("/add/{book_id}/{page_num}/{content}")
async def add_note(book_id: int, page_num: int, content: str):
    """
        Creates a new note associated with a specific book and page number.

        Args:
            book_id (int): Unique identifier of the book the note belongs to.
            page_num (int): Page number in the book where the note is associated with (optional). Defaults to None.
            content (str): The actual content of the note.
    """
    for book in BOOKS:
        if book.id == book_id and 1 <= page_num <= book.pages:
            NOTES.append(Note(get_next_note_id(), book_id, content, page_num, datetime.now(), datetime.now()))
            break


@router.put("/update/{note_id}/{new_content}")
async def update_note(note_id: int, new_content: str):
    """
        Updates the content of an existing note identified by its ID.

        Args:
            note_id (int): Unique identifier of the note to be updated.
            new_content (str): The new content for the note.
    """
    for note in NOTES:
        if note.id == note_id:
            note.content = new_content
            note.updated_at = datetime.now()
            break

@router.delete("/delete/{note_id}")
async def delete_note(note_id: int):
    """
        Deletes the content of an existing note identified by its ID.

        Args:
            note_id (int): Unique identifier of the note to be deleted.
    """
    for note in NOTES:
        if note.id == note_id:
            NOTES.remove(note)
            break


