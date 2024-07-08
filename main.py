from fastapi import FastAPI
import books
import notes
import reading

app = FastAPI()


app.include_router(books.router)
app.include_router(notes.router)
app.include_router(reading.router)





