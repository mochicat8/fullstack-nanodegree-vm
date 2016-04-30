# Provides a number of functions and variables
import sys

from sqlalchemy import Column, ForeignKey, Integer, String

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
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	address = Column(String(250), nullable=False)
	city = Column(String(250), nullable=False)
	zipCode = Column(Varchar(5), nullable=False)
	website = Column(String(250), nullable=False)


class Puppy(Base):
	__tablename__= 'puppy'
	#Mapper Functions
	name = Column(String(80), nullable=False)
	date_of_birth = Column(Date, nullable=False)
	gender = Column(Boolean)
	weight = Column(Varchar(3), nullable=False)
	shelter_id = Column(Integer, ForeignKey('shelter.id'))
	shelter = relationship(Shelter)

#### End
engine = create_engine('sqlite:///puppies.db')
Base.metadata.create_all(engine)