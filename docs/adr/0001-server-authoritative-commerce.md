# ADR 0001: Server-authoritative commerce

## Status
Accepted.

## Decision
The service calculates tenant scope, seller eligibility, item availability, price, discount, tax, currency, order total, refund eligibility and entitlement state on the server. Client-supplied monetary or privilege fields are advisory only and must never override authoritative records.

## Consequences
Orders require immutable snapshots, idempotency keys, auditable state transitions and provider reconciliation. Manual overrides require explicit reasons and privileged approval. This increases implementation effort but prevents client-side price, tenant and entitlement manipulation.
