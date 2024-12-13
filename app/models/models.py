from pydantic.fields import Field

from .base import BaseModel

__all__ = [
    "Browse",
    "BrowseFields"
]


class BrowseFields:
    url = Field(description="URL.", example="https://www.google.com/")


class BaseBrowse(BaseModel):
    """Base model for user."""


class Browse(BaseBrowse):
    url: str = BrowseFields.url
