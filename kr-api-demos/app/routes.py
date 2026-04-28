# This is the API Layer
"""
This is the Controller Layer
FastAPI provides APIRouter, a class used to group related endpoints together
Think of it as a mini-application inside your larger FastAPI app. It helps organize routes cleanly

Imports two Pydantic models (Customer and PredictionResponse) from your app.models module.
Customer likely defines the input schema (fields like age, balance, transactions).
PredictionResponse defines the output schema (probably fields like score and label).
"""

from fastapi import APIRouter
from fastapi import HTTPException
from app.models import Customer, PredictionResponse

"""
Imports a function compute_score from your app.service module.
This function encapsulates the business logic: given customer data, it computes a numeric score and a label.
"""
from app.service import compute_score

import logging

logger = logging.getLogger(__name__)

logger.info("Received prediction request")

"""
creates and instance of APIRouter
All routes defined below will be attached to this router, which can later be included in the main FastAPI app
"""
router = APIRouter()


"""
First endpoint: Home 
@router.get("/") registers a GET endpoint at the root path (/).
When someone visits http://localhost:8000/, this function runs.
It returns a simple JSON response: {"message": "API is Working"}.
Purpose: a health check or “ping” endpoint to confirm the API is alive.
"""


@router.get("/")
def home():
    return {"message": "API is Working"}


"""
Registers a POST endpoint at /predict.
Declares that the response will conform to the PredictionResponse model.
FastAPI will validate and auto‑document this.

The parameter customer: Customer means FastAPI will:
    - Expect a JSON body matching the Customer schema 
    - Parse and validate it automatically 
    - Provide it as a Customer object inside the function.  
"""


@router.post("/predict", response_model=PredictionResponse)
def predict(customer: Customer):
    if customer.balance < 0:
        raise HTTPException(status_code=400, detail="Invalid Balance")
    score, label = compute_score(customer.age, customer.balance, customer.transactions)

    return {"score": score, "label": label}
