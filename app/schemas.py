from pydantic import BaseModel


class RecipeBase(BaseModel):
    title: str
    views: int = 0
    cooking_time: int
    ingredients: str
    instructions: str


class RecipeCreate(RecipeBase):
    pass


class RecipeOut(RecipeBase):
    id: int

    class Config:
        from_attributes = True  # Заменяем orm_mode для Pydantic v2