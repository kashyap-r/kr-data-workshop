# this module represents the schemas
"""
👉 This ensures:

validation
clean contracts (VERY important in interviews)
"""

from pydantic import BaseModel


class Customer(BaseModel):
    age: int
    balance: float
    transactions: int


class PredictionResponse(BaseModel):
    score: float
    label: str
