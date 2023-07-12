books = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
]

sortBooksYearWise = sorted(books,key=lambda x: x['title'], reverse=True)
for book in sortBooksYearWise:
    print(f'Title: {book["title"]}, Author: {book["author"]}, Year: {book["year"]}')

