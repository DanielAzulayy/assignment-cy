from pydantic import BaseModel


# extensibility for words, add more fields in the future.
class Words(BaseModel):
    value: str = None
