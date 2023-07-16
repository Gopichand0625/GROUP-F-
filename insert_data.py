from app import db
from models import Users, Cart, Books, Purchases

def insert_user_data():
 
    users_data = [
        {
            'username': 'john_doe',
            'password': 'mypassword123',
            'fname': 'John',
            'lname': 'Doe',
            'email': 'john@example.com'
        },
        {
            'username': 'jane_smith',
            'password': 'mypassword123',
            'fname': 'Jane',
            'lname': 'Smith',
            'email': 'jane@example.com'
        },
        
    ]

   
    for data in users_data:
        new_user = Users(**data)
        db.session.add(new_user)

def insert_cart_data():
   
    cart_data = [
        {
            'image': 'img_1.jpg',
            'qty': 2,
            'price': 25.0,
            'subTotal': 50.0
        },
        {
            'image': 'img_2.jpg',
            'qty': 3,
            'price': 18.0,
            'subTotal': 54.0
        },
        
    ]

    
    for data in cart_data:
        new_cart_item = Cart(**data)
        db.session.add(new_cart_item)

def insert_purchase_data():
  
    purchases_data = [
        {
            'uid': 'user1',
            'image': 'img_1.jpg',
            'quantity': 1,
            'date': '2023-07-16'
        },
        {
            'uid': 'user2',
            'image': 'img_2.jpg',
            'quantity': 2,
            'date': '2023-07-17'
        },
       
    ]

    
    for data in purchases_data:
        new_purchase = Purchases(**data)
        db.session.add(new_purchase)

def insert_books_data():
  
    books_data = [
        {
            'image': 'img_1.jpg',
            'price': 80.0,
            'onSale': 1,
            'onSalePrice': 15.0,
            'kind': 'Novel'
        },
        {
            'image': 'img_2.jpg',
            'price': 55.0,
            'onSale': 0,
            'onSalePrice': None,
            'kind': 'Non-Fiction'
        },
        {
            'image': 'img_3.jpg',
            'price': 120.0,
            'onSale': 0,
            'onSalePrice': None,
            'kind': 'Fiction'
        },
        {
            'image': 'img_4.jpg',
            'price': 25.0,
            'onSale': 0,
            'onSalePrice': None,
            'kind': 'Non-Fiction'
        },
        {
            'image': 'img_5.jpg',
            'price': 100.0,
            'onSale': 0,
            'onSalePrice': None,
            'kind': 'Non-Fiction'
        },
        {
            'image': 'img_6.jpg',
            'price': 155.0,
            'onSale': 0,
            'onSalePrice': None,
            'kind': 'Scientific'
        },
        {
            'image': 'img_7.jpg',
            'price': 90.0,
            'onSale': 0,
            'onSalePrice': None,
            'kind': 'Fiction'
        },
        {
            'image': 'img_8.jpg',
            'price': 55.0,
            'onSale': 10,
            'onSalePrice': 45.0,
            'kind': 'Non-Fiction'
        },
        {
            'image': 'img_9.jpg',
            'price': 75.0,
            'onSale': 10,
            'onSalePrice': 65.0,
            'kind': 'Fiction'
        }
        
    ]

   
    for data in books_data:
        new_book = Books(**data)
        db.session.add(new_book)


if __name__ == '__main__':
    insert_user_data()
    insert_cart_data()
    insert_purchase_data()
    insert_books_data()


db.session.commit()