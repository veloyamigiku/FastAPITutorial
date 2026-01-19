from fastapi import FastAPI
from fastapi import Query
from pydantic import BaseModel
from pydantic import Field
from typing import Annotated
from typing import Literal

app = FastAPI()

class FilterParams(BaseModel):
  
  model_config = {
    'extra': 'forbid'
  }
  

  limit: int = Field(
    default=100,
    gt=0,
    le=100
  )
  offset: int = Field(
    default=0,
    ge=0
  )
  order_by: Literal['created_at', 'updated_at'] = 'created_at'
  tags: list[str] = []

# Pydantic モデルによるクエリパラメータ
@app.get('/items/')
async def read_items(
  filter_query: Annotated[FilterParams, Query()]
):
  return filter_query
