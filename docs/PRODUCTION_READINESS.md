# Production Readiness Gate

Current decision: **NO-GO**.

Production requires evidence for:

- Running versioned APIs and health endpoints
- Identity, tenant and seller-verification integration
- Payment-provider sandbox and production controls
- Signed webhook, replay and reconciliation tests
- Tax, discount, refund and chargeback test matrices
- Guardian approval for minor accounts
- Cross-tenant, privilege-bypass and price-tampering tests
- English and Tamil content review
- WCAG-aligned accessibility validation
- Load, failure, backup/restore and rollback tests
- Dashboards, alerts, ownership and incident exercises

Documentation alone does not establish production readiness.
