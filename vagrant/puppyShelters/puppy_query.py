from sqlalchemy import create_engine
from sqlalchemy import func
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

print "Printing Name (Alphabetically)"
for instance in session.query(Puppy).order_by(Puppy.name):

    print instance.name + " " +  instance.gender

print "Printing Name (Birth < 6 months)"
for instance in session.query(Puppy).filter(Puppy.dateOfBirth > datetime.date.today() - datetime.timedelta(days = 180)).order_by(-Puppy.dateOfBirth):
    print (instance.name, instance.dateOfBirth.isoformat())

print "Printing Puppy Weight"
for instance in session.query(Puppy).order_by(Puppy.weight):
    print (instance.name, str(round(instance.weight,2)))


print "Printing Puppy Shelter"
for instance1, instance2, instance3 in session.query(Puppy, Shelter, func.count(Puppy.shelter_id)).filter(Puppy.shelter_id == Shelter.id).group_by(Shelter.id).all():
    print (instance2.name, instance3)
