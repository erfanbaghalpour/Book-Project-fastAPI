from fastapi import Body, FastAPI

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


BOOKS = [
    Book(1, "Computer Science Pro", "codingwithroby", "A very nice book", 5),
    Book(2, "The Art of War", "Sun Tzu", "A classic treatise on military strategy", 4),
    Book(3, "To Kill a Mockingbird", "Harper Lee",
         "A Pulitzer Prize-winning novel about racial injustice in the American South", 5),
    Book(4, "The Hitchhiker's Guide to the Galaxy", "Douglas Adams",
         "A hilarious science fiction novel about the misadventures of an unwitting human and his alien friend", 4),
    Book(5, "The Great Gatsby", "F. Scott Fitzgerald", "A novel about the decadence and excess of the Roaring Twenties",
         4),
    Book(6, "Pride and Prejudice", "Jane Austen",
         "A classic romance novel about the trials and tribulations of the Bennet sisters", 5)
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.post("/create_book")
async def create_book(book_request=Body()):
    BOOKS.append(book_request)
