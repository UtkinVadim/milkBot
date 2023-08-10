from pydantic import BaseModel


class BuyerAnswer(BaseModel):
    buyer_id: int
    message: str
