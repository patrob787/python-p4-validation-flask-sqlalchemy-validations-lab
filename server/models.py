from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def validate_name(self, key, name):
        if len(name) < 1:
            raise ValueError("name must be entered")
        return name
    
    @validates('phone_number')
    def validate_phone_number(self, key, number):
        if len(number) != 10:
            raise ValueError('phone number must be 10 digits')
        return number

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('content')
    def validate_content(self, key, body):
        if len(body) < 250:
            raise ValueError("post content must be at least 250 characters")
        return body
    
    @validates('summary')
    def validate_summary(self, key, body):
        if len(body) >= 250:
            raise ValueError("Summary too long, must be 250 characters maximum")
        return body
    
    @validates('category')
    def validate_category(self, key, cat):
        if cat != 'Fiction' and cat != 'Non-Fiction':
            raise ValueError("Category must be Fiction or Non-Fiction")
        return cat
    
    @validates('title')
    def validate_title(self, key, title):
        if "Won't Believe" not in title or "Secret" not in title or "Top" not in title or "Guess" not in title:
            raise ValueError('Title not clickbait-y enough')
        return title


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
