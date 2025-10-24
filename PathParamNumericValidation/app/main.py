from fastapi import FastAPI
from fastapi import Path
from fastapi import Query
from typing import Annotated

app = FastAPI()

# メタデータの宣言
@app.get('/items/{item_id}')
async def read_items(
  item_id: Annotated[int, Path(title='The ID of the item to get')],
  q: Annotated[str | None, Query(alias='item-query')] = None):
  
  results = {'item_id': item_id}
  if q:
    results.update({'q': q})
  return results
# 数値の検証:以上
@app.get('/items/{item_id}/validation1')
async def read_items_validation1(
  item_id: Annotated[int, Path(title='The ID of the item to get', ge=1)],
  q: str):
  
  results = {'item_id': item_id}
  if q:
    results.update({'q': q})
  return results

# 数値の検証:より大きいと以下
@app.get('/items/{item_id}/validation2')
async def read_items_validation2(
  item_id: Annotated[int, Path(
    title='The ID of the item to get',
    gt=0,
    le=1000)],
  q: str):
  
  results = {'item_id': item_id}
  if q:
    results.update({'q': q})
  return results

# 数値の検証:波動小数点、大なり小なり
@app.get('/items/{item_id}/validation3')
async def read_items_validation3(
  item_id: Annotated[int, Path(title='The ID of the item to get', ge=0, le=1000)],
  q: str,
  size: Annotated[float, Query(gt=0, lt=10.5)]):

  results = {'item_id': item_id}
  if q:
    results.update({'q': q})
  if size:
    results.update({'size': size})
  return results
