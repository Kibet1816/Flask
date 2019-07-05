from . import db
from werkzeug.security import generate_password_hash,check_password_hash



class User(db.Model):
    """
    The user model class

    Args:
        DbModel:Connects our class to our database and allow communication
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(300))
    email = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    password = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

    @property
    def password(self):
        """
        Method to create a write only class property
        """
        raise AttributeError("You can\'t read the password attribute")

    @password.setter
    def password(self,password):
        """
        Method to set the password
        """
        self.password = generate_password_hash(password)

    def verify_password(self,password):
        """
        Method to verify password
        """
        return check_password_hash(self.password,password)


