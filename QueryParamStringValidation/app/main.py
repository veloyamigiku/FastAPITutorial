from typing import Annotated
from fastapi import FastAPI
from fastapi import Query

app = FastAPI()

# バリデーションの追加
@app.get('/items')
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
  results = {
    'items': [
      {
        'item_id': 'Foo'
      },
      {
        'item_id': 'Bar'
      }
    ]
  }
  if q:
    results.update({
      'q': q
    })
  return results

# バリデーションをさらに追加する
@app.get('/items_min_length')
async def read_items_min_length(
  q: Annotated[str | None, Query(min_length=3, max_length=50)] = None
):
  results = {
    'items': [
      {
        'item_id': 'Foo'
      },
      {
        'item_id': 'Bar'
      }
    ]
  }
  if q:
    results.update({
      'q': q
    })
  return results

# 正規表現の追加
@app.get('/items_re')
async def read_items_re(
  q: Annotated[str | None, Query(
    min_length=3,
    max_length=50,
    pattern='^fixedquery$')] = None
):
  results = {
    'items': [
      {
        'item_id': 'Foo'
      },
      {
        'item_id': 'Bar'
      }
    ]
  }
  if q:
    results.update({
      'q': q
    })
  return results

# クエリパラメータのリスト / 複数の値
@app.get('/items_list')
async def read_item_list(q: Annotated[list[str] | None, Query()] = None):
  query_items = {'q': q}
  return query_items

# エイリアスパラメータ
@app.get('/items_alias')
async def read_items_alias(q: Annotated[str | None, Query(alias='item-query')] = None):
  results = {
    'items': [
      {
        'item_id': 'Foo'
      },
      {
        'item_id': 'Bar'
      }
    ]
  }
  if q:
    results.update({
      'q': q
    })
  return results

# 非推奨パラメータ
@app.get('/items_deprecated')
async def read_items_deprecated(q: Annotated[
  str | None,
  Query(deprecated=True)] = None):
  results = {
    'items': [
      {
        'item_id': 'Foo'
      },
      {
        'item_id': 'Bar'
      }
    ]
  }
  if q:
    results.update({
      'q': q
    })
  return results
