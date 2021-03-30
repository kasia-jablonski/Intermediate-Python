from sqlalchemy import (create_engine, Column, Integer, String, Date)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///studying.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Study(Base):
    __tablename__ = 'studying'

    id = Column(Integer, primary_key=True)
    date = Column('Date', Date)
    time = Column('Time studied', Integer)
    content = Column('Content Covered', String)

    def __repr__(self):
        return f'Date: {self.date} Total Time Studied: {self.time} Content Covered: {self.content}'