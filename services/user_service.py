import uuid
import datetime

from app import db
from models.user import User
from utils import status


class UserServices:
    def __init__(self):
        return

    def create(self, data):
        user = User(
                publicId=str(uuid.uuid4()),
                email=data.get('email'),
                firstName=data.get('firstName'),
                lastName=data.get('lastName'),
                password=data.get('password'),
                updatedAt=datetime.datetime.utcnow()
            )
        return self.save(user)

    def create_superuser(self, data):
        user = User(
                publicId=str(uuid.uuid4()),
                email=data.get('email'),
                firstName=data.get('firstName'),
                lastName=data.get('lastName'),
                password=data.get('password'),
                isActive=True,
                isStaff=True,
                isAdmin=True,
                updatedAt=datetime.datetime.utcnow()
            )
        return self.save(user)

    def get_by_id(self, id):
        return User.query.filter_by(id=id).first()

    def get_by_publicId(self, publicId):
        return User.query.filter_by(publicId=publicId).first()

    def get_by_email(self, email):
        return User.query.filter_by(email=email).first()

    def get_all_users(self):
        return User.query.all()

    def update_user_by_publicId(self, data: dict, publicId: str = None):
        if publicId is None or publicId == "":
            return {
                "status": "Fail",
                "message": "Missing publicId"
            }, status.HTTP_400_BAD_REQUEST
        
        user = User.query.filter_by(publicId=publicId).first()
        
        firstName = data.get("firstName", None)
        lastName = data.get("lastName", None)
        if firstName or lastName:
            user.firstName = firstName
            user.lastName = lastName
            return self.save(user)
        return user

    def save(self, user):
        db.session.add(user)
        db.session.commit()
        return user