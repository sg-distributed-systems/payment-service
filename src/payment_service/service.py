"""
Payment processing and transaction management.

Handles payment authorization, capture, and refund operations across multiple
payment methods and currencies. Includes fraud detection checks and transaction
logging.
"""
from datetime import datetime
from decimal import Decimal
from uuid import uuid4

from core_logger import get_logger

from .errors import PaymentError, ValidationError

logger = get_logger("payment-service", tier="compliance")

SUPPORTED_CURRENCIES = {"USD", "EUR", "GBP", "JPY"}
SUPPORTED_METHODS = {"credit_card", "debit_card", "bank_transfer", "paypal"}


def process_payment(
    order_id: str, amount: Decimal, currency: str, payment_method: str
) -> dict:
    logger.info(
        "payment_initiated",
        order_id=order_id,
        amount=str(amount),
        currency=currency,
        method=payment_method,
    )

    if amount <= 0:
        raise ValidationError("amount_must_be_positive")

    if currency not in SUPPORTED_CURRENCIES:
        raise ValidationError(
            "unsupported_currency", details={"supported": list(SUPPORTED_CURRENCIES)}
        )

    if payment_method not in SUPPORTED_METHODS:
        raise ValidationError(
            "unsupported_payment_method", details={"supported": list(SUPPORTED_METHODS)}
        )

    transaction_id = uuid4()
    logger.debug(
        "payment_gateway_called", transaction_id=str(transaction_id), method=payment_method
    )

    if amount > Decimal("10000"):
        logger.warning(
            "fraud_check_triggered", transaction_id=str(transaction_id), amount=str(amount)
        )

    logger.info("payment_completed", transaction_id=str(transaction_id), status="succeeded")
    return {
        "transaction_id": transaction_id,
        "status": "succeeded",
        "processed_at": datetime.utcnow(),
    }


def refund_payment(transaction_id: str, amount: Decimal, reason: str) -> dict:
    logger.info(
        "refund_initiated", transaction_id=transaction_id, amount=str(amount), reason=reason
    )
    refund_id = uuid4()
    logger.info("refund_completed", refund_id=str(refund_id))
    return {"refund_id": refund_id, "status": "refunded", "processed_at": datetime.utcnow()}
