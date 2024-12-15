
A simple Flask-based web service that allows users to subscribe with their details (name, email, phone number), 
sends a welcome email to the user, and sends a notification email to the admin. It also supports viewing and deleting subscribers.

Pkg to install:
- Flask
- Flask-Mail
- SQLAlchemy
- Jinja2

DATABASE:

 - database.py
   
Contains the database configuration and session management.
Uses SQLAlchemy to interact with the SQLite database.
The init_db() function initializes the database tables.
Configure your email settings in the app.py file:

- Replace MAIL_USERNAME and MAIL_PASSWORD with your email credentials.
- Update the MAIL_DEFAULT_SENDER to be the same as the MAIL_USERNAME.

Run the Flask application:

  python app.py

The application will be available at http://127.0.0.1:5000.

API EndpointsYou can ou POstaMan to try the APICALL

POST http://127.0.0.1:5000/subscribe

EXE:

{
  "name": "John Doe",
  "email": "johndoe@example.com",
  "phone": "123-456-7890"
}

GET http://127.0.0.1:5000/subscribers:

DELETE /delete_subscriber:

Description: Delete a subscriber by providing their id.

Request Body:

{
  "id": 1
}
