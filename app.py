from flask import Flask, render_template,session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

@app.route("/")
def index():
    books = db.execute("SELECT * FROM books")
    booksLen = len(books)
    # Initialize variables
    shoppingCart = []
    shopLen = len(shoppingCart)
    totItems= 0
    total=0
    display=0
    if 'user' in session:
        shoppingCart = db.execute("SELECT image, SUM(qty), SUM(subTotal), price, id FROM cart")
        shopLen = len(shoppingCart)
        for i in range(shopLen):
            total += shoppingCart[i]["SUM(subTotal)"]
            totItems += shoppingCart[i]["SUM(qty)"]
        books = db.execute("SELECT * FROM books")
        booksLen = len(books)
        return render_template ("index.html", shoppingCart=shoppingCart, books=books, shopLen=shopLen, booksLen=booksLen, total=total, totItems=totItems, display=display, session=session )
    return render_template ( "index.html", books=books, shoppingCart=shoppingCart, booksLen=booksLen, shopLen=shopLen, total=total, totItems=totItems, display=display)

if __name__ == '__main__':
    app.run()