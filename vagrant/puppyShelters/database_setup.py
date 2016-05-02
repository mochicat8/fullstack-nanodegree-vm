# Provides a number of functions and variables
import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Numeric

from sqlalchemy.ext.declarative import declarative_base
#used when having the mapper
from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

#allows python to know it is base for table in the database
Base = declarative_base()


#Object oriented form  of a table in database
#Extends Base class
#Inside table and mapper code

class Shelter(Base):
	__tablename__='shelter'
	#Mapper Functions
	#Establishes a column in the database
	#Attributes are columns
    id = Column(Integer, primary_key = True)
    name =Column(String(80), nullable = False)
    address = Column(String(250))
    city = Column(String(80))
    state = Column(String(20))
    zipCode = Column(String(10))
    website = Column(String)


class Puppy(Base):
	__tablename__= 'puppy'
	#Mapper Functions
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(6), nullable = False)
    dateOfBirth = Column(Date)
    picture = Column(String)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)
    weight = Column(Numeric(10))

#### End
engine = create_engine('sqlite:///puppies.db')
Base.metadata.create_all(engine)