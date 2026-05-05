# Book Library API

A REST API to manage a personal book collection built with FastAPI.

## Setup

1. Clone the repo and navigate to the project directory
2. Create a virtual environment:
```bash
   python -m venv venv
   source venv/bin/activate
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

## Running the server

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

Interactive docs: `http://127.0.0.1:8000/docs`

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/books` | Get all books |
| GET | `/books/{id}` | Get a specific book |
| POST | `/books` | Add a new book to the library |
| PUT | `/books/{id}` | Update a book's details |
| DELETE | `/books/{id}` | Remove a book from the library |

## Creating a book

Send a POST request to `/books` with:
```json
{
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "description": "A fantasy adventure",
  "published_date": "1937-09-21",
  "isbn": "978-0547928227",
  "pages": 310,
  "country": "United Kingdom",
  "count": 2
}
```

Fields:
- `title` — required
- `author` — required
- `published_date` — required (format: YYYY-MM-DD)
- `isbn` — required
- `pages` — required
- `description` — optional
- `country` — optional
- `count` — optional, defaults to 1 (number of copies owned)

The API auto-generates:
- `id` — unique identifier
- `recieved_date` — date the book was added to the library
