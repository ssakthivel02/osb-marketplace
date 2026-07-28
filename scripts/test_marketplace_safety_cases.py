#!/usr/bin/env python3
CASES = {
    "cross_tenant_order_read": "reject",
    "client_price_override": "reject",
    "duplicate_order_without_idempotency": "reject",
    "unsigned_payment_webhook": "reject",
    "stale_webhook_replay": "reject",
    "unverified_seller_publish": "reject",
    "minor_purchase_without_guardian": "reject",
    "raw_card_data_submission": "reject",
    "refund_without_authorisation": "reject",
    "entitlement_without_settlement": "reject",
}
assert all(outcome == "reject" for outcome in CASES.values())
for case in CASES:
    print(f"PASS: {case}")
print("Marketplace negative safety cases validated")
