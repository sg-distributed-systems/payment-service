# payment-service

Handles payment processing and transaction management.

## Why this repo exists

Payment processing requires strict isolation for PCI compliance, independent scaling during high-traffic periods, and specialized error handling.

## Core Components

### `process_payment(order_id: str) -> bool`
Initiates payment processing for an order.

**Logs:**
- `payment_attempted` — Logged when a payment attempt begins

### `fail_payment(order_id: str, reason: str)`
Records a payment failure with the associated reason.

**Logs:**
- `payment_failed` — Logged when a payment fails, includes the order ID and failure reason

## HTTP Interface

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/healthz` | GET | Liveness probe |
| `/readyz` | GET | Readiness probe |
| `/payments/process` | POST | Processes a payment |

### Running the service

```bash
uvicorn src.payment_service.app:app --host 0.0.0.0 --port 8004
```
