from sqlalchemy import Column, Integer, String
from app.db.base import Base

class XPTO(Base):
  __tablename__ = 'xpto2'
  id    = Column('id', Integer, primary_key=True, autoincrement=True)
  name  = Column('name', String, nullable=False)
