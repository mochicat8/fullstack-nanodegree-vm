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

class Restaurant(Base):
	__tablename__='restaurant'
	#Mapper Functions
	#Establishes a column in the database
	#Attributes are columns
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)

class MenuItem(Base):
	__tablename__= 'menu_item'
	#Mapper Functions
	name = Column(String(80), nullable=False)
	id = Column(Integer, primary_key=True)
	description = Column(String(250))
	price = Column(String(8))
	course = Column(String(250))
	restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
	restaurant = relationship(Restaurant)

#### End
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
