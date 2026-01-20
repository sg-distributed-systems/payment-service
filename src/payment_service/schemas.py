"""
Pydantic models for API request and response validation.

Defines data transfer objects used for request parsing and response
serialization in the API layer.
"""
from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, Field


class ProcessPaymentRequest(BaseModel):
    order_id: str
    amount: Decimal = Field(gt=0)
    currency: str
    payment_method: str


class ProcessPaymentResponse(BaseModel):
    transaction_id: UUID
    status: str
    processed_at: datetime
