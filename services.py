from models import Subscriber
from database import get_session
from sqlalchemy.exc import IntegrityError

class SubscriberService:
    
    @staticmethod
    def subscribe(name, email, phone):
        """Subscribe a new user."""
        try:
            session = get_session()

            # Check if the email already exists
            existing_subscriber = session.query(Subscriber).filter_by(email=email).first()
            if existing_subscriber:
                return {"error": "Email already exists. Please use a different email."}, 400

            # Create a new subscriber
            new_subscriber = Subscriber(name=name, email=email, phone=phone)
            session.add(new_subscriber)
            session.commit()
            session.close()

            return {"message": "Subscription successful."}, 200

        except IntegrityError:
            session.rollback()  # Rollback the session if there’s a database integrity error
            return {"error": "Database error occurred."}, 500
        except Exception as e:
            return {"error": f"Error: {str(e)}"}, 500

    @staticmethod
    def delete_subscriber(subscriber_id):
        """Delete an existing subscriber."""
        try:
            session = get_session()

            # Find the subscriber by ID
            subscriber_to_delete = session.query(Subscriber).filter_by(id=subscriber_id).first()
            if not subscriber_to_delete:
                return {"error": "Subscriber not found."}, 404

            # Delete the subscriber from the database
            session.delete(subscriber_to_delete)
            session.commit()
            session.close()

            return {"message": "Subscriber deleted successfully."}, 200

        except Exception as e:
            return {"error": f"Error: {str(e)}"}, 500

    @staticmethod
    def get_all_subscribers():
        """Get the list of all subscribers."""
        try:
            session = get_session()
            subscribers = session.query(Subscriber).all()
            session.close()

            # Convert list of subscribers to list of dictionaries
            subscribers_list = [{
                'id': subscriber.id,
                'name': subscriber.name,
                'email': subscriber.email,
                'phone': subscriber.phone
            } for subscriber in subscribers]

            return subscribers_list, 200

        except Exception as e:
            return {"error": f"Error: {str(e)}"}, 500