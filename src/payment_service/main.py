from core_logger import get_logger

logger = get_logger("payment-service")


def process_payment(order_id: str) -> bool:
    logger.info("payment_attempted", order_id=order_id)
    return True


def fail_payment(order_id: str, reason: str) -> None:
    logger.error("payment_failed", order_id=order_id, reason=reason)


def main() -> None:
    process_payment("order-001")
    fail_payment("order-002", "insufficient_funds")


if __name__ == "__main__":
    main()
