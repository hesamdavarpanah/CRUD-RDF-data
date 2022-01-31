from typing import Optional, List

from pydantic import BaseModel


# input entity model
class Entity(BaseModel):
    description: Optional[str] = None
    label: Optional[str] = None
    lang: Optional[str] = None
    aliases: Optional[List[str]] = []


# input data model
class Data(BaseModel):
    id: str
    main_fields: List[Entity]
