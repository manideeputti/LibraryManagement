from flask import Flask, request, jsonify
from models import Book, Member
from Database import Books, Members

app = Flask(__name__)

@app.route('/Books', methods=['POST'])
def add_book():
    data = request.json
    if not data or 'Book_name' not in data or 'Author' not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    new_book = Book(Book_id=len(Books) + 1, Book_name=data['Book_name'], Author=data['Author'])
    Books.append(new_book)
    return jsonify({"message": "Book added successfully"}), 201

@app.route('/Books/<int:book_id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(book_id):
    book = next((b for b in Books if b.Book_id == book_id), None)
    if not book:
        return jsonify({"error": f"Book with id {book_id} not found"}), 404

    if request.method == 'GET':
        return jsonify(book.__dict__)

    if request.method == 'PUT':
        data = request.json
        book.Book_name = data.get('Book_name', book.Book_name)
        book.Author = data.get('Author', book.Author)
        return jsonify({"message": "Book updated successfully"}), 200

    if request.method == 'DELETE':
        Books.remove(book)
        return jsonify({'message': "Book deleted successfully"}), 200

@app.route('/Members', methods=['GET', 'POST'])
def manage_members():
    if request.method == 'POST':
        data = request.json
        if not data or 'Name' not in data or 'Age' not in data or 'Gender' not in data:
            return jsonify({"error": "Invalid input"}), 400
        
        new_member = Member(Id=len(Members) + 1, Name=data['Name'], Age=data['Age'], Gender=data['Gender'])
        Members.append(new_member)
        return jsonify({"message": "Member added successfully"}), 201

    if request.method == 'GET':
        return jsonify([member.__dict__ for member in Members])

@app.route("/Books/Search", methods = ['GET'])
def search_books() :
  data = request.json
  query = data['query'].lower()
  results = [book.__dict__ for book in Books if query in book.Book_name.lower() or query in book.Author.lower()]
  return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
