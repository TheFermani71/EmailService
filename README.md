A simple Flask-based web service that allows users to subscribe with their details (name, email, phone number), sends a welcome email to the user, and sends a notification email to the admin. It also supports viewing and deleting subscribers.

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
Features
User Subscription: Allows users to subscribe with their name, email, and phone number.
Email Notifications: Sends a welcome email to the user and a notification email to the admin upon a new subscription.
Subscriber Management: View all subscribers and delete a subscriber by their ID.
Error Handling: Graceful error handling for invalid requests and database errors.
Installation
Prerequisites
Make sure you have Python 3.6+ installed on your system. You also need an email service (e.g., Gmail) to send the emails.

Clone the repository:

bash
Copia codice
git clone https://github.com/yourusername/subscriber-management.git
cd subscriber-management
Install dependencies:

bash
Copia codice
pip install -r requirements.txt
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
Code Structure
The code is structured into multiple files to improve organization and maintainability:

bash
Copia codice
.
├── app.py                # Main application file with Flask routes
├── database.py           # Database initialization and session handling
├── models.py             # SQLAlchemy models
├── services.py           # Subscriber service logic
├── requirements.txt      # Required Python packages
├── templates/            # Folder for email templates
│   ├── welcome_email.html
│   └── notification_email.html
└── README.md             # Project documentation
app.py
This is the main entry point of the application.
It sets up the Flask app, the email configuration, and the routes for handling subscriptions, deletion, and retrieving subscribers.
It imports the SubscriberService to handle the logic of subscribing, deleting, and getting subscribers.
database.py
Contains the database configuration and session management.
Uses SQLAlchemy to interact with the SQLite database.
The init_db() function initializes the database tables.
models.py
Defines the Subscriber class that maps to the subscribers table in the database.
Uses SQLAlchemy ORM to define the structure of the table and provide a way to interact with the data.
services.py
Contains the business logic for subscribing, deleting, and fetching subscribers.
This class encapsulates the database queries and handles errors gracefully.
The SubscriberService class includes the following methods:
subscribe(name, email, phone): Subscribes a new user.
delete_subscriber(subscriber_id): Deletes a subscriber by their id.
get_all_subscribers(): Returns a list of all subscribers.
Email Templates
The templates/ folder contains the HTML templates used for email notifications:

welcome_email.html: The email template sent to the user upon subscription.
notification_email.html: The email template sent to the admin upon a new subscription.
How the Technologies Are Used
Flask: Flask is used to create the RESTful API and handle HTTP requests such as subscribing, deleting, and fetching subscribers.
SQLAlchemy: SQLAlchemy is used to interact with the SQLite database. It provides an Object-Relational Mapping (ORM) layer for Python to easily work with database tables and execute queries.
Flask-Mail: Flask-Mail is used to send emails (welcome and notification emails). It integrates with your Gmail account (or any other email service) to send HTML emails.
Jinja2: Jinja2 is used as the templating engine for rendering the HTML email templates with dynamic content such as the subscriber's name and phone number.
License
This project is open-source and available under the MIT License. See the LICENSE file for more details.

Conclusion
This setup allows you to manage subscribers effectively while sending notifications both to the user and to the admin. The modular structure of the project ensures that you can easily extend it by adding new features or modifying existing ones.

Let me know if you need additional features or help with anything else!
