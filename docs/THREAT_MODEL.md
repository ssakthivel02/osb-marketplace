# Marketplace Threat Model

## Assets
Orders, seller identity, prices, entitlements, refunds, payment-provider tokens and audit evidence.

## Principal threats
- Cross-tenant listing, order or entitlement access
- Price or currency tampering
- Duplicate order submission
- Forged payment or refund webhooks
- Seller impersonation and fraudulent listings
- Child purchase without guardian approval
- Credential or payment-card data leakage
- Refund abuse, chargeback abuse and replay attacks
- Privileged manual override without audit

## Mandatory controls
Server-authoritative tenant and price calculation, authenticated seller actions, verified sellers, idempotency keys, signed provider webhooks, bounded replay windows, provider tokenisation, guardian checks for minors, dual approval for high-value manual refunds, immutable order snapshots, rate limits and tamper-evident audit logs.
