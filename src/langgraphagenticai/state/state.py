from pydantic import BaseModel
from typing_extensions import List, TypedDict
from langgraph.graph.message import add_messages
from typing import Annotated


class State(TypedDict):
    """represent the structure of the state insisde the graph"""
    messages: Annotated[List,add_messages]