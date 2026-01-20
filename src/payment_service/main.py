"""
Service entrypoint with lifecycle management.

Initializes configuration, correlation ID, and signal handlers before running
the main service logic. Provides structured error handling for all exceptions.
"""
from core_logger import get_logger

from payment_service.config import load_config
from payment_service.errors import AppError
from payment_service.lifecycle import install_signal_handlers
from payment_service.observability import init_correlation_id

logger = get_logger("payment-service")


def process_payment(order_id: str) -> bool:
    logger.info("payment_attempted", order_id=order_id)
    return True


def fail_payment(order_id: str, reason: str) -> None:
    logger.error("payment_failed", order_id=order_id, reason=reason)


def run() -> None:
    cfg = load_config("payment-service")
    cid = init_correlation_id()
    install_signal_handlers("payment-service")

    logger.info("service_starting", env=cfg.env, correlation_id=cid)

    try:
        process_payment("order-001")
        fail_payment("order-002", "insufficient_funds")
        logger.info("service_completed")
    except AppError as e:
        logger.warning("app_error", **e.to_log_fields())
        raise
    except Exception as e:
        logger.exception("unhandled_exception", exc=e)
        raise


def main() -> None:
    run()


if __name__ == "__main__":
    main()
