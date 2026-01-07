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
