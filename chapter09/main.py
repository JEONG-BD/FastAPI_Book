from enum import Enum
from typing import Optional
from uuid import UUID
from datetime import datetime, time, timedelta
from fastapi import FastAPI, Query, Path, Body, Cookie, Header, File, Form, Header
from pydantic import BaseModel, Field, HttpUrl
from typing import List

app = FastAPI()

# FAKE_ITEM_DB = [{'item_name': 'Foo'},
#                 {'item_name': 'Bar'},
#                 {'item_name': 'Baz'}]
#
#
# class FootEnum(str, Enum):
#     fruit = 'fruit'
#     vegetables = 'vegetables'
#     dairy = 'dairy'
#
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#
# # uvicorn main:app --reload
#
# @app.get('/', description='This is our first route', tags=['Test'], deprecated=True)
# async def root():
#     return {'message':'hello world'}
#
#
# @app.post('/', tags=['Test'], deprecated=False)
# async def post():
#     return {'message':'hello from post route'}
#
#
# @app.put('/', tags=['Test'])
# async def put():
#     return {'message':'hello from put route'}
#
#
# #@app.get('/items', tags=['Item'])
# #async def list_items(skip: int = 0, limit: int = 10):
#     #return FAKE_ITEM_DB[skip:skip+limit]
#     #return {'message':'list items route'}
#
#
# @app.get('/items/{item_id}', tags=['Item'])
# async def get_item(item_id: str, q: Optional[str] = None, short: bool = False):
#     item = {'item_id': item_id}
#
#     if q:
#         item.update({'q': q})
#     if not short:
#         item.update(
#             {
#                 'description': 'Test Test Test Test'
#             }
#         )
#         #return {'item_id': item_id, 'q':q}
#     #return {'item_id': item_id}
#     #return {'message':item_id}
#     return item
#
#
# @app.post('/items', tags=['Item'])
# async def create_items(item: Item) -> Item:
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({'price_with_tax': price_with_tax})
#         print(item_dict)
#     return item_dict
#
# @app.put('/items/{item_id}', tags=['Item'])
# async def create_items(item_id: int, item: Item, q: str | None = None):
#     result = {'item_id':item_id, **item.dict()}
#     if q:
#         result.update({'q': q})
#     return result
#
#
# @app.get('/items', tags=['Item'])
# async def read_items(remark: str | None = Query(..., min_length=3, max_length=10, description='This is a sample query string', alias='item-query')):
#     result = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
#     if remark:
#         result.update({'remark': remark})
#     return result
#
#
# @app.get('/items_hidden', tags=['Item'])
# async def hidden_items(hidden_query: str | None = Query(None, include_in_schema=False)):
#     if hidden_query:
#         return {'hidden_query': hidden_query}
#     return {'hidden_query': 'Not found'}
#
#
# @app.get('/items_validation/{item_id}', tags=['Item'])
# async def read_item_validation(
#         *,
#         item_id: int = Path(..., title='The ID of the item to get', ge=10, le=100),
#         q: str | None = Query(None, alias='item-query'), size: float = Query(..., gt=0, lt=7.75)):
#
#     result = {'item_id': item_id, 'size': size}
#
#     if q:
#         result.update({'q': q})
#     return result
#
#
# @app.get('/users', tags=['User'])
# async def list_users():
#     return {'message':'list items route'}
#
#
# @app.get('/users/current', tags=['User'])
# async def get_current_user():
#     return {'message':'this is the current user'}
#
#
# @app.get('/users/{user_id}', tags=['User'])
# async def get_user(user_id: str):
#     return {'message':user_id}
#
#
# @app.get('/foods/{food_name}', tags=['Food'])
# async def get_food(food_name : FootEnum):
#     if food_name == FootEnum.vegetables:
#         return {'food_name': food_name, 'message': 'you are healthy'}
#
#     if food_name.value == 'fruit':
#         return {
#             'food_name': food_name,
#             'message': 'you are still healthy but like sweet things'
#         }
#     return {
#         'food_name': food_name,
#         'message': 'I like chocolate milk'
#     }
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#
#
# class User(BaseModel):
#     firstname: str
#     lastname: str | None = None
#
#
# class Importance(BaseModel):
#     importance: int
#
# @app.put('/items/{item_id}')
# async def item(*,
#                item_id: int = Path(..., title='The Id of the item to get', ge=0, le=150),
#                q: str | None = None,
#                item: Item | None = None,
#                user: User,
#                importance: int = Body(..., embed=True)):
#
#     result = {'item_id':item_id}
#     if q:
#         result.update({'q': q})
#     if item:
#         result.update({'item': item})
#     if user:
#         result.update({'user': user})
#     if importance:
#         result.update({'importance':importance})
#     return result

# class Item(BaseModel):
#     name: str
#     description: str | None = Field(title='The Description of the item', max_length=300)
#     price: float = Field(..., gt=0, description='The price must be greater than zero')
#
#
# @app.put('/items/{item_id}', tags=['Item'])
# async def update_item(item_id : int, item: Item = Body(..., embed=True)):
#     result = {'item_id': item_id, 'item': item}
#     return result

#
# class Image(BaseModel):
#     url: HttpUrl
#     name: str
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     # tags: list[str] = []
#     tags: set[str] = []
#     image: list[Image] | None = None
#
# class Offer(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     items: list[Item]
#
#
# @app.put('/item/{item_id}', tags=['Item'])
# async def update_item(item_id: int, item: Item):
#     result = {'item_id': item_id, 'item': item}
#     return result
#
#
# @app.post('/offers', tags=['ETC'])
# async def create_offer(offer: Offer = Body(..., embed=True)):
#     return offer
#
#
# @app.post('/images/multiple', tags=['ETC'])
# async def create_multiple_images(images: list[Image]):
#     return images

# class Item(BaseModel):
#     name: str
#     description: str | None
#     price: float
#     tax: float | None

    # name: str = Field(..., example='Foo')
    # description: str | None = Field(..., example='A very nice Item')
    # price: float = Field(..., example=16.25)
    # tax: float | None = Field(..., example=1.67)

    # class Config :
    #     schema_extra = {
    #         'example': {
    #             'name': 'Foo',
    #             'description': 'A very nice Item',
    #             'price': 16.25,
    #             'tax': 1.67
    #         }
    #     }

# @app.put('/item/{item_id}', tags=['Item'])
# async def update_item(
#         item_id: int,
#         item: Item = Body(
#             ...,
#             openapi_examples={
#                 'normal': {
#                     'name': 'Foo',
#                     'description': 'A very nice Item',
#                     'price': 16.25,
#                     'tax': 1.67
#                 },
#                 'converted': {
#                     'summary': 'Amn example with converted data',
#                     'description': 'FastAPI can convert price `string` to actual `numbers` automatic',
#                     'value': {'name': 'Bar', 'price': '16.25'}
#                 },
#                 'invalid': {
#                     'summary': 'Invalid data is rejected with an error',
#                     'value': {'name': 'Baz', 'price': 'sixteen point two five'}
#                 }
#             }
#         )
#     ):
#     result = {'item_id': item_id, 'item': item}
#     return result


@app.put('/items/{item_id}')
async def read_items(item_id: UUID,
                     start_date: datetime | None = Body(None),
                     end_date: datetime | None = Body(None),
                        repeat_at: time | None = Body(None),
                        process_after : timedelta | None = Body(None),
                     ):
    start_process = start_date + process_after
    duration = end_date - start_process
    return {'item_id': item_id,
            'start_date': start_date,
            'end_date': end_date,
            'repeat_at': repeat_at,
            'process_after': process_after,
            'start_process': start_process,
            'duration': duration
            }