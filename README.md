
A simple Flask-based web service that allows users to subscribe with their details (name, email, phone number), 
sends a welcome email to the user, and sends a notification email to the admin. It also supports viewing and deleting subscribers.

Table of Contents

Technologies Used
Features
Installation
Usage
API Endpoints
Code Structure

Technologies Used

Python: A high-level, interpreted programming language.
Flask: A micro web framework for Python to build the backend API.
SQLAlchemy: An Object Relational Mapper (ORM) for Python to interact with the SQLite database.
SQLite: A lightweight, serverless relational database used for storing subscriber data.
Flask-Mail: A Flask extension for sending email notifications.
Jinja2: A templating engine used to create HTML email templates.

Here's a list of required packages:

Flask
Flask-Mail
SQLAlchemy
Jinja2

Create an App Password for your Gmail account (if using Gmail) to avoid issues with authentication. Refer to Gmail App Passwords.

Configure your email settings in the app.py file:

Replace MAIL_USERNAME and MAIL_PASSWORD with your email credentials.
Update the MAIL_DEFAULT_SENDER to be the same as the MAIL_USERNAME.
Initialize the database by running the init_db() method in app.py.

Run the Flask application:

bash
Copia codice
python app.py
The application will be available at http://127.0.0.1:5000.

Usage
Once the server is running, you can use Postman or any HTTP client to interact with the API.

API Endpoints
POST /subscribe:

Description: Subscribe a new user by providing name, email, and phone.
Request Body:
json
Copia codice
{
  "name": "John Doe",
  "email": "johndoe@example.com",
  "phone": "123-456-7890"
}
Response:
Success:
json
Copia codice
{
  "message": "Subscription successful."
}
Error (Email exists):
json
Copia codice
{
  "error": "Email already exists. Please use a different email."
}
GET /subscribers:

Description: Retrieve a list of all subscribers.
Response:
json
Copia codice
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "johndoe@example.com",
    "phone": "123-456-7890"
  }
]
DELETE /delete_subscriber:

Description: Delete a subscriber by providing their id.
Request Body:
json
Copia codice
{
  "id": 1
}
Response:
Success:
json
Copia codice
{
  "message": "Subscriber deleted successfully."
}
Error (Subscriber not found):
json
Copia codice
{
  "error": "Subscriber not found."
}
