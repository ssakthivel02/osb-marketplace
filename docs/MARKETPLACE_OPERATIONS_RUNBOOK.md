# Marketplace Operations Runbook

## Incidents
1. Freeze affected listing, seller or tenant scope.
2. Preserve order, webhook, refund and entitlement evidence.
3. Rotate compromised provider secrets and reject stale signatures.
4. Reconcile provider settlement against internal orders.
5. Notify security, finance, safeguarding and support owners as applicable.
6. Restore service only after tenant-isolation, pricing and entitlement checks pass.

## Recovery checks
- No cross-tenant data exposure
- No price or currency mutation after purchase
- Idempotency prevents duplicate orders and refunds
- Payment and refund webhooks are signed and within replay window
- Entitlements match successfully settled orders
- Refund and chargeback ledgers reconcile
- English and Tamil customer journeys remain usable

## Rollback
Disable new purchases, preserve read-only order history, revoke affected releases, restore the last validated policy and run reconciliation before reopening checkout.
