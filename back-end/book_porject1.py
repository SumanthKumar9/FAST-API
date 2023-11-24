from fastapi import FastAPI
from fastapi import Body
app = FastAPI()


Books =[
	{"id":"1","name":"Book1","authour":"sumanth1","category":"math","publish Data":"2021-9-19"},
	{"id":"2","name":"Book2","authour":"sumanth2","category":"math","publish Data":"2022-9-19"},
	{"id":"3","name":"Book3","authour":"sumanth3","category":"science","publish Data":"2023-9-19"},
	{"id":"4","name":"Book4","authour":"sumanth4","category":"science","publish Data":"2024-9-19"},
	{"id":"5","name":"Book5","authour":"sumanth5","category":"history","publish Data":"2025-9-19"}
]

@app.get("/books")
def read_all_books():
	return Books

@app.get("/books/{name}")
def read_books_by_title_and_category(name,category:str):
	books_to_return =[]
	for i in Books:
		if i.get('name') == name and i.get('category') == category:
			books_to_return.append(i)
	return books_to_return	
	
@app.get("/books/{dynamic_param}")
def get_book_by_id(dynamic_param:str):
	for i in Books:
		if i.get('id') == dynamic_param:
			return i
			
@app.get("/books/")
def read_category_by_query(category:str):
	books_to_return = []
	for i in Books:
		if i.get("category") == category:
			books_to_return.append(i)
	return books_to_return
	
@app.post("/books/create_book")
def create_book(new_book = Body()):
	Books.append(new_book)

@app.put("/books/update_book")
def update_book(book=Body()):
	for i in range(len(Books)):
		if Books[i].get('id').casefold() == book.get('id').casefold():
			Books[i] = book
			break
			
@app.delete("/books/{id}")
def delete_book_by_id(id:str):
	for i in range(len(Books)):
		if Books[i].get('id').casefold() == id.casefold():
			Books.pop(i)
			break
















