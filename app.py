from flask import Flask, request, jsonify, render_template
from database import init_db, get_session 
#from sqlalchemy.exc import IntegrityError
from flask_mail import Mail, Message
from models import Subscriber

# Initialize Flask app
app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-pass'
app.config['MAIL_DEFAULT_SENDER'] = 'emailservice1997@gmail.com'  # Default sender for emails

# Initialize Flask-Mail
mail = Mail(app)

# Initialize the database
init_db()


@app.route('/subscribe', methods=['POST'])
def subscribe():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json."}), 400

    data = request.get_json()
    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    phone = data.get('phone', '').strip()

    if not name or not email or not phone:
        return jsonify({"error": "Name,email and phone are required."}), 400

    try:
        # Get a new database session
        session = get_session()

        # Check if the email already exists in the database
        existing_subscriber = session.query(Subscriber).filter_by(email=email).first()
        if existing_subscriber:
            return jsonify({"error": "Email already exists. Please use a different email."}), 400

        # Save the new subscriber in the database
        new_subscriber = Subscriber(name=name, email=email, phone=phone)
        session.add(new_subscriber)
        session.commit()

        # Send the welcome email to the user and the notification email
        send_welcome_email(name, email, phone)
        send_notification_email(name, email, phone)

        session.close()

        return jsonify({"message": "Welcome email and notification sent successfully!"}), 200
    except Exception as e:
        print(f"Error sending email: {e}")
        return jsonify({"error": "Failed to send welcome email."}), 500

def send_welcome_email(name, email, phone):
    subject = "Benvenuto"
    html_content = render_template('welcome_email.html', name=name, phone=phone, current_year=2024)

    msg = Message(subject=subject, recipients=[email], html=html_content)
    mail.send(msg)

def send_notification_email(name, email, phone):
    subject = "New Subscription Notification"
    html_content = render_template('notification_email.html', name=name, email=email, phone=phone, current_year=2024)

    # Send notification email to the admin (or email service)
    msg = Message(subject=subject, recipients=['emailservices1997@gmail.com'], html=html_content)
    mail.send(msg)


    # Route to get the list of subscribers
@app.route('/subscribers/list', methods=['GET'])
def get_subscribers():
    try:
        # Get a new database session
        session = get_session()

        # Fetch all subscribers from the database
        subscribers = session.query(Subscriber).all()
        
        # Convert the list of subscribers into a list of dictionaries
        subscribers_list = [{
            'id': subscriber.id,
            'name': subscriber.name,
            'email': subscriber.email,
            'phone': subscriber.phone
        } for subscriber in subscribers]

        session.close()

        return jsonify(subscribers_list), 200
    except Exception as e:
        print(f"Error fetching subscribers: {e}")
        return jsonify({"error": "Failed to fetch subscribers."}), 500
    

    # Route to delete a subscriber
@app.route('/delete_subscriber', methods=['DELETE'])
def delete_subscriber():
    # Check if the request content type is JSON
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json."}), 400

    # Try to get the data from the request JSON body
    data = request.get_json()

    # Check if the 'id' key exists in the JSON payload
    subscriber_id = data.get('id')
    if not subscriber_id:
        return jsonify({"error": "ID is required to delete the subscriber."}), 400

    try:
        # Get a new session
        session = get_session()

        # Try to find the subscriber with the provided id
        subscriber_to_delete = session.query(Subscriber).filter_by(id=subscriber_id).first()

        # If no subscriber is found, return an error
        if not subscriber_to_delete:
            return jsonify({"error": "Subscriber not found."}), 404

        # If subscriber is found, delete it
        session.delete(subscriber_to_delete)
        session.commit()

        # Close the session after the operation
        session.close()

        return jsonify({"message": "Subscriber deleted successfully."}), 200
    except Exception as e:
        # If any error occurs, return an error message
        print(f"Error: {e}")
        return jsonify({"error": "Failed to delete subscriber."}), 500



if __name__ == '__main__':
    app.run(debug=True)