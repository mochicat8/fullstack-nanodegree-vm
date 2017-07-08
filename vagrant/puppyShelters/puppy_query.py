from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from puppies import Base, Shelter, Puppy
#from flask.ext.sqlalchemy import SQLAlchemy
from random import randint
import datetime
import random


engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


for instance in session.query(Puppy).order_by(Puppy.name):
    print instance.name + " " +  instance.gender


for instance in session.query(Puppy).filter(Puppy.dateOfBirth > datetime.date.today() - datetime.timedelta(days = 180)).order_by(-Puppy.dateOfBirth):
    print (instance.name, instance.dateOfBirth)
