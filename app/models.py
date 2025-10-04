from sqlalchemy import Column, Integer, String, Text

from app.database import Base


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    views = Column(Integer, default=0)
    cooking_time = Column(Integer)
    ingredients = Column(Text)
    instructions = Column(Text)
