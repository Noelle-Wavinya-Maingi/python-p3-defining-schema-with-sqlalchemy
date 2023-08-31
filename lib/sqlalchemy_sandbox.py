#!/usr/bin/env python3
# Import necessary modules
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

#Create a declarative base
Base = declarative_base()

#Define the student class
class Student(Base):
    #Define students table name
    __tablename__ =  'students'

#Define columns for the table
    id = Column(Integer(), primary_key = True)
    name = Column(String())

#Check if the script is being run as the main program
if __name__ == '__main__':
    #Create a db engine using SQLite and connect it to the students.db
    engine = create_engine('sqlite:///students.db')
    #Create the tables define by the classes that inherit from Base
    Base.metadata.create_all((engine))