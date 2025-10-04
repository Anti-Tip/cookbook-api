from pydantic import BaseModel, ConfigDict


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

    model_config = ConfigDict(from_attributes=True)
