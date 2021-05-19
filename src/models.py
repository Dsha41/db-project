import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(50), primary_key=True)
    phone = Column(Integer, nullable=False)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(Integer, nullable=False)
   
    country = Column(String(250), nullable=False)
    city = Column(String(250), nullable=False)


    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    
   

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.user_name,
            "name": self.name,
            "lastname": self.last_name,
            "streetname": self.street_name,
            "streetnumber": self.street_number,
            "postcode": self.post_code,
            "country": self.country,
            "city": self.city
        }

class PhotoAdd(Base):
        __tablename__ = 'photoadd'
        id = Column(Integer, primary_key=True)
        
        
        person = relationship(Person)
        person_id = Column(Integer, ForeignKey('person.id'))
        
        def to_dict(self):
            return {
            "id": self.id,
            "person": self.person,
            "personID": self.person_id
        }
        

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))   
    person = relationship(Person)

    def to_dict(self):
        return {
            "id": self.id,
            "person": self.person,
            "personID": self.person_id
        }

class Interaction(Base):
    __tablename__ = 'interaction'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    follower_id = Column(Integer, ForeignKey('follower.id'))
    like = Column(Integer, nullable=True)
    comment =  Column(String(250), nullable=True)
    follower = relationship(Follower)

    def to_dict(self):
        return {
            "id": self.id,
            "postID": self.post_id,
            "followerId": self.follower_id,
            "like": self.like,
            "comment": self.comment,
            "follower": self.follower
        }

class Post(Base):
        __tablename__ = 'post'
        id = Column(Integer, primary_key=True)
        footer_description = Column(String(250), nullable=False)
        person_id = Column(Integer, ForeignKey('person.id'))
        person = relationship(Person)
        
        place =  Column(String(250), nullable=False)
        photo_add_id = Column(Integer, ForeignKey('photoadd.id'))
        photo_add = relationship(PhotoAdd)
        interaction_id = Column(Integer, ForeignKey('interaction.id'))
        interaction = relationship(Interaction)
        
        def to_dict(self):
            return {
            "id": self.id,
            "person": self.person,
            "personID": self.person_id,
            "description": self.footer_description,
            "place": self.place,
            "photoAddID": self.photo_add_id,
            "photoAdd": self.photo_add,
            "interactionID": self.interaction_id,
            "interaction": self.interaction

        }



       
        
    

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e