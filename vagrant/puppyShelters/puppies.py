# Provides a number of functions and variables
import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, Date

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
	__tablename__= 'shelter'
	id = Column(Integer, primary_key = True)
	name =Column(String(80), nullable = False)
	address = Column(String(250))
	city = Column(String(250))
	state = Column(String(250))
	zipCode = Column(String(250))
	website = Column(String(250))


class Puppy(Base):
	__tablename__= 'puppy'
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	gender = Column(String(250), nullable = False)
	dateOfBirth = Column(Date)
	picture = Column(String(250))
	shelter_id = Column(Integer, ForeignKey('shelter.id'))
	shelter = relationship(Shelter)
	weight = Column(Numeric)
#
# #### End
engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.create_all(engine)
