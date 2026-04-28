# this module contains the business logic

"""
👉 This is where:

        ML model will go later
        Feature engineering happens
"""
import logging
logger = logging.getLogger(__name__)

def compute_score(age: int, balance: float, transactions: int):
    logger.info(f"Computing score for balance={balance}" )
    score = (balance / 1000) + transactions * 0.1

    if score > 10:
        label = "High value"
    else:
        label = "Low value"

    return score, label
