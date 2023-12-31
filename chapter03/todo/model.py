from typing import List, Optional
from pydantic import BaseModel
from fastapi import Form 

class Todo(BaseModel):
    id : Optional[int] = None
    item : str 
    
    @classmethod
    def as_form(cls, item: str = Form(...)):
        return cls(item=item)


class TodoItem(BaseModel):
    item : str 
    
    class Config : 
        schema_extra = {
            'example': {
                'item' : 'Read the next chater of the book'
            }
        }


class TodoItems(BaseModel):
    todos : List[TodoItem]
    
    class Config:
        schema_extra = {
            'example': {
                'todos':[
                    {
                        'item':'Example Schema 1!'
                    }, 
                    {
                        'item':'Example Schema 2!'
                    },
                    {
                        'item':'Example Schema 3!'
                    },
                ]
            }
        }
