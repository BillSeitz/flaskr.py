from sqlalchemy import Column, Integer, String, Text
from database import Base

class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True)
    text = Column(Text(), unique=True)

    def __init__(self, title=None, text=None):
        self.title = title
        self.text = text

    def __repr__(self):
        return '<Entry %r>' % (self.title)
