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
    birthday = Column(Integer, nullable=False)
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
            "email": self.email,
            "phone": self.phone,
            "lastname": self.last_name,
            "streetname": self.street_name,
            "streetnumber": self.street_number,
            "postcode": self.post_code,
            "birthday": self.birthday,
            "country": self.country,
            "city": self.city
        }

class PhotoAdd(Base):
        __tablename__ = 'photoadd'
        id = Column(Integer, primary_key=True)
        images = Column(String(20), nullable=False)
        
        person_id = Column(Integer, ForeignKey('person.id'))
        person = relationship(Person)
        
        def to_dict(self):
            return {
            "id": self.id,
            "person": self.person,
            "personID": self.person_id,
            "images": self.images
        }

class History(Base):
        __tablename__ = 'history'
        id = Column(Integer, primary_key=True)
        history = Column(String(20), nullable=False)
        vacune = Column(String(20), nullable=False)
        person_id = Column(Integer, ForeignKey('person.id'))
        person = relationship(Person)
        
        def to_dict(self):
            return {
            "id": self.id,
            "person": self.person,
            "personID": self.person_id,
            "vacune": self.vacune,
            "history": self.history
        }

class Pet(Base):
    __tablename__ = 'pet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    race = Column(String(20), nullable=False)
    gender = Column(String(50), nullable=True)
    age = Column(Integer, nullable=False)
    species = Column(String(250), nullable=False)
    weight = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    birthday = Column(Integer, nullable=False)
    person = relationship(Person)
    person_id = Column(Integer, ForeignKey('person.id'))
    photo_add_id = Column(Integer, ForeignKey('photoadd.id'))
    photo_add = relationship(PhotoAdd)
    history_id = Column(Integer, ForeignKey('history.id'))
    history = relationship(History)

    def to_dict(self):
            return {
            "id": self.id,
            "name": self.name,
            "race": self.race,
            "gender": self.gender,
            "age": self.age,
            "species": self.species,
            "weight": self.weight,
            "height": self.height,
            "birthday": self.birthday,
            "photoAddID": self.photo_add_id,
            "photoAdd": self.photo_add,
            "historyID": self.history_id,
            "history": self.history,
            "person": self.person,
            "personID": self.person_id
        }

class Guess(Base):
    __tablename__ = 'guess'
    id = Column(Integer, primary_key=True)
    pet = relationship(Pet)
    pet_id = Column(Integer, ForeignKey('pet.id'))

    def to_dict(self):
            return {
            "id": self.id,
            "pet": self.pet,
            "petID": self.pet_id
        }

class Interaction(Base):
    __tablename__ = 'interaction'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    like = Column(Integer, nullable=True)
    comment =  Column(String(250), nullable=True)
    guess_id = Column(Integer, ForeignKey('guess.id'))
    guess = relationship(Guess)

    def to_dict(self):
        return {
            "id": self.id,
            "postID": self.post_id,
            "guessId": self.guess_id,
            "like": self.like,
            "comment": self.comment,
            "guess": self.guess
        }



class Post(Base):
        __tablename__ = 'post'
        id = Column(Integer, primary_key=True)
        footer_description = Column(String(250), nullable=False)
        person_id = Column(Integer, ForeignKey('person.id'))
        person = relationship(Person)
        place =  Column(String(250), nullable=False)
        date = Column(Integer, nullable=False)
        pet = relationship(Pet)
        pet_id = Column(Integer, ForeignKey('pet.id'))
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
            "interaction": self.interaction,
            "pet": self.pet,
            "petID": self.pet_id

        }



       
        
    

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e