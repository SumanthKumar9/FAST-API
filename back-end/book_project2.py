from fastapi import FastAPI,Body,Path,Query,HTTPException
from pydantic import BaseModel,Field
from typing import Optional
from starlette import status

app = FastAPI()

class Book:
	id: int
	title: str
	authour: str
	description: str
	ratng: int
	published_date :int

	def __init__(self,id,title,authour,description,rating,published_date):
		self.id = id
		self.title = title
		self.authour = authour
		self.description = description
		self.rating = rating
		self.published_date = published_date

class BookRequest(BaseModel):
	id: Optional[int]=None
	title: str = Field(min_length=3)
	authour: str = Field(min_length=3)
	description: str = Field(max_length=100)
	rating: int = Field(gt=0,lt=6)
	published_date:int = Field(gt=1999,lt=2099)

	class Config:
		json_schema_extra = {
			'example':{
				'title':'A new Book',
				'authour' : 'sumanth',
				'description' : 'a coding book',
				'rating' : 3,
				'published_date' :2012
			}
		}

Books =[
	Book(1,'Computer Science','sumanth','A Book',5,2012),
	Book(2,'Mathematics','with kumar','A very Great Book',1,2013),
	Book(3,'English','sumanth','Book',3,2015),
	Book(4,'DAA','achari',' Great Book',2,2012),
	Book(5,'DBMS','chanti',' Great Book',4,2013)
]


@app.get("/book",status_code=status.HTTP_200_OK)
def read_all_books():
	return Books


@app.get("/book/{book_id}",status_code=status.HTTP_200_OK)
def get_book_by_id(book_id:int = Path(gt=0)):
	for i in Books:
		if i.id == book_id:
			return i
	raise HTTPException(status_code = 404,detail="Item not found")


@app.get("/book/",status_code=status.HTTP_200_OK)
def get_books_by_rating(book_rating:int = Query(gt=0,lt=6)):
	books_to_return = [i for i in Books if i.rating == book_rating]
	return books_to_return


@app.get('/book/published_date/',status_code=status.HTTP_200_OK)
def get_books_by_published_date(published_date:int = Query(gt=1999,lt=2099)):
	books_to_return = [i for i in Books if i.published_date == published_date]
	return books_to_return


@app.post("/book/create_book",status_code =  status.HTTP_201_CREATED)
def add_new_book(book_request:BookRequest):
	new_book =Book(**book_request.dict())
	Books.append(find_book_id(new_book))


def find_book_id(book:Book):
	book.id = 1 if len(Books) == 0 else  Books[-1].id + 1
	return book


@app.put("/books/update_book",status_code = status.HTTP_204_NO_CONTENT)
def update_book(updated_book:BookRequest):
	book_changed = False
	for i in range(len(Books)):
		if Books[i].id == updated_book.id:
			Books[i] = updated_book
			book_changed = True
			break
	if not book_changed:
		raise HTTPException(status_code=404,detail="Item not found")


@app.delete("/books/{id}",status_code = status.HTTP_204_NO_CONTENT)
def delete_book_by_id(id:int = Path(gt=0)):
	book_changed = False
	for i in range(len(Books)):
		if Books[i].id == id:
			Books.pop(i)
			book_changed = True
			break
	if not book_changed:
		raise HTTPException(status_code=404,detail="Item not found")
